import threading
import queue
import time 
q = queue.Queue()

 
def numbers_in_Q(q):
    flag = True
    while flag:
        for i in range(100):
              q.put(i)
        print("1, qsize", q.qsize())
        time.sleep(0.01)

 
def print_letters(q):

    arr = []
    flag = True
    while flag:
        for i in range(100):
            arr.append(q.get())

        print(arr)
        print("2 q",q.qsize())
        q.task_done()
        arr.clear()
        time.sleep(2)
 
thread1 = threading.Thread(target=numbers_in_Q, args=(q,))
thread2 = threading.Thread(target=print_letters,  args=(q,))
 
thread1.start()
thread2.start()
 
thread1.join()
thread2.join()