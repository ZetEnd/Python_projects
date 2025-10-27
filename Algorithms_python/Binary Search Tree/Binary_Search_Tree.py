def search(root, key):

    if root is not None or root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)

    return search(root.left)


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):

    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root

        if root.val < key:
            root.right = insert(root.right, key)

        if root.val > key:
            root.left = insert(root.left, key)

    return root

def inorder(root):

    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


if __name__ == "__main__":
    r = Node(50)

    r = insert(r, 30)
    r = insert(r, 40)
    r = insert(r, 80)
    r = insert(r, 20)
    r = insert(r, 70)
    r = insert(r, 60)


    r = insert(r,30)


    inorder(r)