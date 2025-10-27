import sys

sys.setrecursionlimit(2000)

class Node:
    def __init__(self, key, depth=0):
        self.key = key
        self.left = None
        self.right = None
        self.depth = depth

class BST:
    def __init__(self):
        self.root = None

    def add(self, node, key, depth=0):
        if node is None:
            if self.root is None:
                self.root = Node(key, depth)
            return Node(key, depth), "DONE"

        if key == node.key:
            return node, "ALREADY"
        elif key < node.key:
            node.left, msg = self.add(node.left, key, depth + 1)
        else:
            node.right, msg = self.add(node.right, key, depth + 1)
        return node, msg

    def search(self, node, key):
        if node is None:
            return "NO"
        if key == node.key:
            return "YES"
        elif key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    def print_tree(self, node):
        if node is None:
            return
        self.print_tree(node.left)
        print('.' * node.depth + str(node.key))
        self.print_tree(node.right)

bst = BST()

def main():
    import sys
    input_lines = sys.stdin.read().splitlines()

    for line in input_lines:
        if not line.strip():
            continue
        parts = line.split()
        cmd = parts[0]
        if cmd == "ADD":
            num = int(parts[1])
            _, msg = bst.add(bst.root, num)
            print(msg)
        elif cmd == "SEARCH":
            num = int(parts[1])
            print(bst.search(bst.root, num))
        elif cmd == "PRINTTREE":
            bst.print_tree(bst.root)

if __name__ == "__main__":
    main()


