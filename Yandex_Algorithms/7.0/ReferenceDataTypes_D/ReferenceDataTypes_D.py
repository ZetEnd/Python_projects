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


def ADD_name(head, n):
    if head == None:

        stack = [n, None, None] 

        stack[1] = stack
        stack[2] = stack

        head = stack
    elif head[1] == None:
        stack = head

        new = [n, head, head]

        stack[1] = new
        stack[2] = new

        head = new

    else:

        h = head

        stack = head

        while stack[1] != head:
            stack = stack[1] 

        new = [n, head, stack]

        stack[1] = new

        h[2] = new

        head = new

        #stack[1] = [n ,None, back]


    #print(head)

    return head[0], head

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
    res = []
    for i in range(N):
        s = input().split()

        if s[0] == "Run":
            if len(s) != 1:
                symbol = s[1]
            else:
                flag = True
                res.append("")
                continue
            for ch in s[2:]:
                symbol += (" " + ch)
            num, head = ADD_name(head, symbol)
            res.append(num)


            #print(s)
            #print(s[0])
        elif s[0][0] == "A":
            count = 0
            if head == None and flag:
                res.append("")
                continue
            for i in range(len(s[0])):
                if s[0][i] == "T":
                    count +=1
            #print(count)
            num, head = Tab(head, count)
            res.append(num)

    for r in res:
        print(r)

