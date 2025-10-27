

def Push_back(head, n):
    if head == None:
        stack = [None, None, None] 


        stack[0] = n 
        head = stack
    else:
        stack = head
        back = head
        while stack[1] != None:
            back = stack
            stack = stack[1] 

        stack[1] = [n ,None, back]

    return "ok", head


def Push_front(head, n):
    if head == None:
        stack = [None, None, None] 


        stack[0] = n 
        head = stack
    else:
        stack = head
        head = [n, head, None]

    return "ok", head


def Pop_back(stack):

    head = stack
    if stack == None:
        return "error", head
    if stack[1] == None:
        n = stack[0]
        del stack 
        return n , None
    else:
        while stack[1] != None:
            back = stack
            stack = stack[1]

        n = stack[0] 

        back[1] = None 

        del stack
        #stack.clear()


        return n, head


def Pop_front(stack):

    if stack == None:
        return "error", None
    if stack[1] == None:
        n = stack[0]
        del stack 
        return n , None
    else:
        head = stack[1]

        n = stack[0] 

        del stack

        return n, head



def Back(stack):
    head = stack

    if stack == None:
        return "error", head
    else:
        while stack[1] != None:
            stack = stack[1]


        return stack[0], head

def Front(stack):
    head = stack

    if stack == None:
        return "error", head
    else:
        return stack[0], head



def Size(stack):

    head = stack

    if stack == None:
        return 0, head
    else:
        n = 1
        while stack[1] != None:
            stack = stack[1] 
            n+=1

        return n, head

def Clear(stack):
    head = stack

    if stack == None:
        return "ok", None
    else:

        while stack != None:
            back = stack 

            stack = stack[1] 

            del back


    return "ok", None

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


def Tab(head, n):

    now = head

    for _ in range(n):
        now = now[1]

    if now == head:

        return now[0], head
    else:
        #print(head)
        down = now[2] 
        up = now[1]

        down[1] = up 

        up[2] = down

        #num = now[0]

        num, head = ADD_name(head, now[0])

        #print("ds",num)
        return num, head

if __name__ == "__main__":

    N = int(input())

    head = None
    res = [0] * N
    arr = [0]
    changed = False
    flag = True
    size = N

    mas = list(map(int, input().split()))
    for i in range(N):


            changed, head = ADD_name(head, mas[i], i)



    real = {}
    num_circle = 1

    while size!= 2 and len(arr) != 0:
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

