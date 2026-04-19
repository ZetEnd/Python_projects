class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def print_inorder(root):

    if root:

        print_inorder(root.left)

        print(root.val)

        print_inorder(root.right)

def print_postorder(root):

    if root is not None:

        print_postorder(root.left)

        print_postorder(root.right)

        print(root.val)

def print_preorder(root):

    if root is not None:

        print(root.val)

        print_preorder(root.left)

        print_preorder(root.right)

if __name__ == "__main__":
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    print_inorder(root)
    print("")
    print_postorder(root)
    print("")
    print_preorder(root)