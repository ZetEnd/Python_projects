class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':

    listt = LinkedList()

    listt.head = Node(10)

    first = listt.head

    second = Node(20)

    first.next = second

    first.data = 15
    listt.printList()
    #print(second.data)
