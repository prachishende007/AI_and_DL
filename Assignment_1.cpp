#include <bits/stdc++.h>
using namespace std;

#define N 3

// Directions: Left, Right, Up, Down
int row[] = {0, 0, -1, 1};
int col[] = {-1, 1, 0, 0};

// Structure for puzzle state
struct PuzzleState {
    vector<vector<int>> board;
    int x, y, depth;

    PuzzleState(vector<vector<int>> b, int i, int j, int d)
        : board(b), x(i), y(j), depth(d) {}
};

// Goal checker
bool isGoalState(const vector<vector<int>>& board) {
    vector<vector<int>> goal = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};
    return board == goal;
}

// Move validity
bool isValid(int x, int y) {
    return (x >= 0 && x < N && y >= 0 && y < N);
}

// Print board
void printBoard(const vector<vector<int>>& board) {
    for (auto& row : board) {
        for (int num : row)
            cout << num << " ";
        cout << endl;
    }
    cout << "--------" << endl;
}

// BFS implementation
void solvePuzzleBFS(vector<vector<int>> start, int x, int y) {
    queue<PuzzleState> q;
    set<vector<vector<int>>> visited;

    q.push(PuzzleState(start, x, y, 0));
    visited.insert(start);

    while (!q.empty()) {
        PuzzleState curr = q.front(); q.pop();

        printBoard(curr.board);

        if (isGoalState(curr.board)) {
            cout << "Goal reached at depth " << curr.depth << " using BFS\n";
            return;
        }

        for (int i = 0; i < 4; i++) {
            int newX = curr.x + row[i];
            int newY = curr.y + col[i];

            if (isValid(newX, newY)) {
                vector<vector<int>> newBoard = curr.board;
                swap(newBoard[curr.x][curr.y], newBoard[newX][newY]);

                if (visited.find(newBoard) == visited.end()) {
                    visited.insert(newBoard);
                    q.push(PuzzleState(newBoard, newX, newY, curr.depth + 1));
                }
            }
        }
    }

    cout << "No solution found using BFS.\n";
}

// Recursive DFS with backtracking
bool dfsRecursive(vector<vector<int>> board, int x, int y, int depth, int maxDepth, set<vector<vector<int>>>& visited) {
    if (depth > maxDepth) return false;

    printBoard(board);

    if (isGoalState(board)) {
        cout << "Goal reached at depth " << depth << " using DFS\n";
        return true;
    }

    visited.insert(board);

    for (int i = 0; i < 4; i++) {
        int newX = x + row[i];
        int newY = y + col[i];

        if (isValid(newX, newY)) {
            vector<vector<int>> newBoard = board;
            swap(newBoard[x][y], newBoard[newX][newY]);

            if (visited.find(newBoard) == visited.end()) {
                if (dfsRecursive(newBoard, newX, newY, depth + 1, maxDepth, visited))
                    return true;
            }
        }
    }

    visited.erase(board); // Backtrack
    return false;
}

// DFS Wrapper
void solvePuzzleDFS(vector<vector<int>> start, int x, int y, int maxDepth = 20) {
    set<vector<vector<int>>> visited;
    if (!dfsRecursive(start, x, y, 0, maxDepth, visited)) {
        cout << "No solution found using DFS within depth " << maxDepth << ".\n";
    }
}

// Main
int main() {
    // Simple test case (2 moves from goal)
    vector<vector<int>> start = {
        {1, 2, 3},
        {4, 5, 6},
        {0, 7, 8}
    };

    // Locate 0 position
    int x, y;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            if (start[i][j] == 0) {
                x = i;
                y = j;
            }

    cout << "Initial State:\n";
    printBoard(start);

    cout << "\n--- Solving with BFS ---\n";
    solvePuzzleBFS(start, x, y);

    cout << "\n--- Solving with DFS ---\n";
    solvePuzzleDFS(start, x, y, 20);

    return 0;
}
