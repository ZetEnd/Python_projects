
def ADD_n(tree, n):

    global myfile

    if len(tree) == 0:
        tree.append(n)
        tree.append([])
        tree.append([])

        #print("DONE")
        myfile.write("DONE\n")
        return
    else:

        if n == tree[0]:
            #print("ALREADY")
            myfile.write("ALREADY\n")
            return 
        elif n < tree[0]:
            ADD_n(tree[1],n)
        else:
            ADD_n(tree[2],n)
    return 

def SEARCH_n(tree, n):
    global myfile

    if len(tree) == 0:
        #print("NO")
        myfile.write("NO\n")
        return 
    else:
        if n == tree[0]:
            #print("YES")
            myfile.write("YES\n")
            return
        elif n < tree[0]:
            SEARCH_n(tree[1],n)
        else:
            SEARCH_n(tree[2],n)
    
    return 


def PRINTTREE(tree,n):
    global myfile

    n +=1
    if len(tree) != 0:
        PRINTTREE(tree[1],n)
        #print(n)
        for i in range(n):
            myfile.write(".")
            #print(".",end = '')
        myfile.write(f"{tree[0]}\n")
        #print(tree[0])
        PRINTTREE(tree[2],n)

    n-=1




if __name__ == "__main__":

    msa = []
    flag = True

    myfile = open("H_tree.txt", "w+")

    while flag:

        #word = input().split()

        parts = input().strip()

        #word = input().split()
        word = parts.split()
        #print(parts)

        if word:

            if word[0] == "ADD":
                ADD_n(msa, int(word[1]))
            elif word[0] == "SEARCH":
                SEARCH_n(msa, int(word[1]))
            elif word[0] == "PRINTTREE":
                PRINTTREE(msa,-1)
        else:
            flag = False

    myfile.seek(0)
    #print(myfile)
    #print(myfile)
    for line in myfile:
        print(line, end = '')
    myfile.close()