
def ADD_n(tree, n):

    if len(tree) == 0:
        tree.append(n)
        tree.append([])
        tree.append([])

        print("DONE")

        return
    else:

        if n == tree[0]:
            print("ALREADY")

            return 
        elif n < tree[0]:
            ADD_n(tree[1],n)
        else:
            ADD_n(tree[2],n)
    return 

def SEARCH_n(tree, n):

    if len(tree) == 0:
        print("NO")

        return 
    else:
        if n == tree[0]:
            print("YES")

            return
        elif n < tree[0]:
            SEARCH_n(tree[1],n)
        else:
            SEARCH_n(tree[2],n)
    
    return 


def PRINTTREE(tree,n):


    n +=1
    if len(tree) != 0:
        PRINTTREE(tree[1],n)
        #print(n)
        for i in range(n):

            print(".",end = '')

        print(tree[0])
        PRINTTREE(tree[2],n)

    n-=1


msa = []
flag = True

while flag:

    parts = input().strip()

    #word = input().split()
    word = parts.split()
    print(parts)
    if word:

        if word[0] == "ADD":
            ADD_n(msa, int(word[1]))
        elif word[0] == "SEARCH":
            SEARCH_n(msa, int(word[1]))
        elif word[0] == "PRINTTREE":
            PRINTTREE(msa,-1)
    else:
        flag = False