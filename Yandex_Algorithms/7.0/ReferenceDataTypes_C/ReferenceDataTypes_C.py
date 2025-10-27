
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

if __name__ == "__main__":
    s = ""
    #stack = [None, None, None]  push_back 
    head = None
    res = []
    while True:
        s = input().split()

        if s[0] == "push_front":
            N = int(s[1])

            num, head = Push_front(head, N)
            res.append(num)

        if s[0] == "push_back":
            N = int(s[1])

            num, head = Push_back(head, N)
            res.append(num)

        if s[0] == "pop_front":

            num, head = Pop_front(head)
            res.append(num)

        if s[0] == "pop_back":

            num, head = Pop_back(head)
            res.append(num)

        if s[0] == "front":
            num, head = Front(head)
            res.append(num)

        if s[0] == "back":
            num, head = Back(head)
            res.append(num)

        if s[0] == "size":

            num, head = Size(head)
            res.append(num)


        if s[0] == "clear":

            num, head = Clear(head)
            res.append(num)

        if s[0] == "exit":
            res.append("bye")
            break

    for r in res:
        print(r)
