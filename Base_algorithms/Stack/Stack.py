
def Stack():
    #LIFO
    stack = []

    stack.append('a')
    stack.append('b')
    stack.append('c')
    print("stack in the beginning")
    print(stack)

    print("\nDrop elements")
    print(stack.pop())
    print(stack.pop())

    print("\nFinal stack")
    print(stack)


def Queue():
    #FIFO
    queue = []

    queue.append('a')
    queue.append('b')
    queue.append('c')
    print("queue in the beginning")
    print(queue)

    print("\nDrop elements")
    print(queue.pop(0))
    print(queue.pop(0))

    print("\nFinal queue")
    print(queue)


class PriorutyQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ''.join(str(i) for i in self.queue)

    def isempty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            max_i = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_i]:
                    max_i = i

            item = self.queue[max_i]
            #del self.queue[max_i]
            self.queue.remove(self.queue[max_i])
            return item

        except IndexError:
            print("error")
            exit()

if __name__ == "__main__":
    #Stack()
    #Queue()

    pqueue = PriorutyQueue()
    pqueue.insert(10)
    pqueue.insert(8)
    pqueue.insert(20)
    pqueue.insert(15)

    while not pqueue.isempty():
        print(pqueue.delete())