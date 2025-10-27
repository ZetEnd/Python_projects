

def ADD_name(head, n, size):
    if head == None:

        stack = [n, None, None,0] 

        stack[1] = stack
        stack[2] = stack

        head = stack
    elif head[1] == None:
        stack = head

        new = [n, head, head, 1]

        stack[1] = new
        stack[2] = new

        #head = new

    else:

        h = head

        stack = head

        #while stack[1] != head:
        for _ in range(size-1):
            stack = stack[1] 

        new = [n, head, stack,size]

        stack[1] = new

        h[2] = new

        #head = new

        #stack[1] = [n ,None, back]


    #print(head)

    return head[0], head


def Check1(head, size):

    now = head
    res = []

    for i in range(size):
        forward = now[1][0]
        behind = now[2][0]

        if now[0] < forward and now[0] <behind:
            res.append(now[3])

        now = now[1]
    return res

def Check(head, size):

    now = head
    res = []
    curr = -1
    first_elem = -1

    for i in range(size):

        forward = now[1]
        if curr == -1:
            behind = now[2]
        else:
            behind = curr

        if i == size-1 and first_elem != -1:
            forward = first_elem

        if now[0] < forward[0] and now[0] <behind[0]:

            if i == 0:
                first_elem = [now[0]]

            res.append(now[3])

            behind[1] = forward 
            forward[2] = behind 

            if now == head:
                head = forward

            curr = [now[0]]

            #del now 
        else:
            curr = -1


        now = now[1]

    return res, head
def poop(head, number):

    now = head
    while now[3] != number:
        now = now[1]

    forward = now[1]
    behind = now[2]

    behind[1] = forward 
    forward[2] = behind 

    if now == head:
        head = forward

    del now 

    return head

if __name__ == "__main__":

    N = int(input())

    head = None
    res = [0] * N
    arr = [0]
    changed = False
    flag = True
    size = N

    mas = list(map(int, input().split()))
    #for i in range(N):


            #changed, head = ADD_name(head, mas[i], i)


    num_circle = 1
    while size!= 2 and len(arr) != 0:

        curr = -1
        first_elem = -1

        lenM = len(mas)
        i = 0
        for i in range(lenM):
            if mas[i] == -1:
                continue

            if curr == -1:
                beh = mas[i-1] 
            else:
                beh = curr

            if i == lenM-1:
                forw = mas[0] 
            else:
                forw = mas[i+1]

            if i == lenM-1 and first_elem != -1:
                forw = first_elem

            if mas[i] < beh and mas[i] < forw:
                res[i] = num_circle
                curr = res[i]

                if i == 0:
                    first_elem = mas[i]

                mas[i] = -1

        while i < lenM:
            if mas[i] == -1:
                mas.pop(i)
            else:
                i+=1
        num_circle +=1

    real = {}
    num_circle = 1

    while size!= 2 and len(arr) != 0 and False:
        arr, head = Check(head,size)

        for a in arr:
            real[a] = num_circle
            res[a] = num_circle


            #head =  poop(head, a)

        num_circle +=1

        size -= len(arr) 

        #if (size == 2 or len(arr) == 0):
            #flag = False
            #changed = 0
            #break

    for r in res:
        print(r, end = " ")


