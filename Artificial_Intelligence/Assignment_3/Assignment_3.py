class KnowledgeBase:
    def __init__(self):
        self.parent = {}   # parent -> [children]
        self.gender = {}   

    def add_parent(self, p, c):
        self.parent.setdefault(p, []).append(c)

    def add_father(self, f, c):
        self.gender[f] = "male "
        self.add_parent(f, c)

    def add_mother(self, m, c):
        self.gender[m] = "  female"
        self.add_parent(m, c)

    def is_parent(self, p, c):
        return c in self.parent.get(p, [])

    def is_sibling(self, a, b):
        for kids in self.parent.values():
            if a in kids and b in kids and a != b:
                return True
        return False

    def is_ancestor(self, a, b):
        if self.is_parent(a, b):
            return True
        for child in self.parent.get(a, []):
            if self.is_ancestor(child, b):
                return True
        return False


def main():
    kb = KnowledgeBase()
    print("Enter facts and queries (e.g. father(Jay,Minal), sibling(Rahul,Raj)?). Enter ,stop, to quit.")
    while True:
        try:
            line = input("> ").strip().replace(" ", "")
            if line == "stop":
                break
        except EOFError:
            break
        if not line:
            continue

        query = line.endswith("?")
        if query:
            line = line[:-1]

        rel = line[:line.find("(")]
        args = line[line.find("(") + 1 : line.find(")")]
        parts = args.split(",")
        A = parts[0]
        B = parts[1] if len(parts) > 1 else None

        if not query:  # add fact
            if rel == "parent":
                kb.add_parent(A, B)
            elif rel == "father":
                kb.add_father(A, B)
            elif rel == "mother":
                kb.add_mother(A, B)
            elif rel in ("male", "female"):
                kb.gender[A] = rel
            print("Fact added.")
        else:  # query
            ans = False
            if rel == "parent":
                ans = kb.is_parent(A, B)
            elif rel == "sibling":
                ans = kb.is_sibling(A, B)
            elif rel == "ancestor":
                ans = kb.is_ancestor(A, B)
            print("Yes" if ans else "No")


if __name__ == "__main__":
    main()
