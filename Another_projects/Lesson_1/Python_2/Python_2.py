# -*- coding: utf-8 -*-
# связной список

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LindedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, data):
        self.head = Node(data, self.head)

    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    def get_last_node(self):
        n = self.head
        while(n.next != None):
            n = n.next
        return n.data

    def is_empty(self):
        return self.head == None

    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end = " => ")
            n = n.next
        print() 


"""
 основной алгоритм
x = myList.head
while x.next != None
  print(x.data)
  x = x.next
"""
s = LindedList()
s.add_to_front(5)
s.add_at_end(8)
s.add_to_front(9)

s.print_list()
print(s.get_last_node())

#Граф
class Graph():
    def __init__(self, size):
        self.adj = [ [0] * size for i in range(size)]
        self.size = size

    def add_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Invalid Edge")
        else:
            self.adj[orig -1][dest -1] = 1
            self.adj[dest -1][orig -1] = 1

    def remove_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Invalid Edge")
        else:
            self.adj[orig -1][dest -1] = 0
            self.adj[dest -1][orig -1] = 0

    def Display(self):
        for row in self.adj:
            print()
            for val in row:
                print('{:4}' .format(val) , end = "")

G = Graph(4)
G.add_edge(1,3)
G.add_edge(3,4)
G.add_edge(2,4)
G.Display()

print()

puf = [ [0] * 5 for i in range(4)]
for row in puf:
            print()
            for val in row:
                print(val , end = "")