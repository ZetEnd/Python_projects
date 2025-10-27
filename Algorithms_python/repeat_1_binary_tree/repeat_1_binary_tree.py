class Node():
    def __init__(self,data = None):
        self.left = None
        self.right = None
        self.data = data

    def add_data(self,data):
        self.data = data

    def add_left(self,node):
        self.left = node

    def add_right(self,node):
        self.right = node

    def print_data(self):
        print(self.data)


def insert(root, key):

    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root

        if root.data < key:
            root.left = insert(root.left, key)

        if root.data > key:
            root.right = insert(root.right, key)

    return root


def print_inorder(root):

    if root is not None:
        print_inorder(root.left)
        print(root.data)
        print_inorder(root.right)

def search(root,data):

    if root is not None or root.data == data:
        return root

    if root.data < data:
         return search(root.right, data)

    return search(root.left, data)

if __name__ == "__main__":

    S = Node()
    S.add_data(5)
    S.print_data()

    S.add_left(Node(3))
    SS = S.left 
    SS.print_data()

    r = Node(50)
    r = insert(r,20)
    r = insert(r,60)
    r = insert(r,30)

    print_inorder(r)