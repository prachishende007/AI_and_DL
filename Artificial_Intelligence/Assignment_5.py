import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  # (row, col)
        self.parent = parent      # pointer to parent node
        self.g = g  # cost from start
        self.h = h  # heuristic cost to goal
        self.f = g + h  # total cost

    def __lt__(self, other):  # needed for heapq
        return self.f < other.f

def heuristic(a, b):
    """Heuristic: Manhattan distance"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    """A* Algorithm for pathfinding on a grid"""
    open_list = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == goal:
            # Reconstruct path
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # reverse path

        closed_set.add(current_node.position)

        # Explore neighbors (4 directions)
        for d_row, d_col in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor_pos = (current_node.position[0] + d_row, current_node.position[1] + d_col)

            # Check boundaries
            if not (0 <= neighbor_pos[0] < len(grid) and 0 <= neighbor_pos[1] < len(grid[0])):
                continue
            # Skip obstacles
            if grid[neighbor_pos[0]][neighbor_pos[1]] == 1:
                continue
            # Skip visited
            if neighbor_pos in closed_set:
                continue

            g_cost = current_node.g + 1
            h_cost = heuristic(neighbor_pos, goal)
            neighbor_node = Node(neighbor_pos, current_node, g_cost, h_cost)

            # Add neighbor to open list
            heapq.heappush(open_list, neighbor_node)

    return None  # no path found


# Example Grid (0 = free, 1 = blocked)
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # Top-left
goal = (4, 4)   # Bottom-right

path = astar(grid, start, goal)
print("Path found:", path)