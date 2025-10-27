
def Push(head, n):
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


    #print(head)

    return "ok", head

def Pop(stack):

    head = stack
    if stack == None:

        #print(head)
        return "error", head
    if stack[1] == None:
        n = stack[0]
        del stack 

        #print(stack)
        return n , None
    else:
        while stack[1] != None:
            back = stack
            stack = stack[1]

        n = stack[0] 

        back[1] = None 

        del stack
        #stack.clear()

        #print(head)
        return n, head


def Back(stack):
    head = stack

    if stack == None:
        return "error", head
    else:
        while stack[1] != None:
            stack = stack[1]


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
    #stack = [None, None, None]
    head = None
    res = []
    while True:
        s = input().split()

        if s[0] == "push":
            N = int(s[1])

            num, head = Push(head, N)
            res.append(num)

        if s[0] == "pop":

            num, head = Pop(head)
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

