

def ADD_n(n):

    global tree

    mas = []

    if tree == None:
        tree = BinTree(n,0, None, None,None)
        #mas.append(tree)

        #print(tree.key)

    else:
        print("ss")
        mas.append(tree)
        while mas:
            print(mas)
            knot = mas[0]

            if mas[0].key == n:
                print("ALREADY")

            if mas[0].key > n:
                if mas[0].right == None:
                    mas[0] = BinTree(mas[0].key,mas[0].deep, mas[0].left, BinTree(n,0,None, None, mas[0]), mas[0].papa)
                    #mas[0].right = BinTree(n,0,None, None, mas[0])
                    print("DONE")
                    print(knot)
                else:
                    mas.append(mas[0].right)
            
            if mas[0].key < n:
                if mas[0].left == None:
                    mas[0] = BinTree(mas[0].key,mas[0].deep, BinTree(n,0,None, None, mas[0]), mas[0].right, mas[0].papa)
                    #mas[0].left = BinTree(n,0,None, None, mas[0])
                    print("DONE")
                    print(mas[0])
                else:
                    mas.append(mas[0].left)

            mas.pop(0)


def PRINTTREE():

    global tree

    mas = [tree] 
    posesheniy = []
    print(mas)

    while mas:

        #s = mas.pop(0)
        #if s not in posesheniy:
        #    print(s.key)
        #    posesheniy.append(s)

        if mas[0].right != None and mas[0].right not in posesheniy:
            mas.append(mas[0].right)
            mas.pop(1)

        if mas[0].left != None and mas[0].left not in posesheniy:
            mas.append(0,mas[0].left)
            mas.pop(1)
        else:
            if mas[0] not in posesheniy:
                print(mas[0].key)
                posesheniy.append(mas[0])
                #mas.pop(0)
        if mas[0].papa != None and mas[0].papa not in posesheniy:
            mas.insert(0,mas[0].papa)
            mas.pop(1)
        #if s.right != None and s.right not in posesheniy:
        #    mas.append(s.right)


if __name__ == "__main__":
    from collections import namedtuple

    BinTree = namedtuple('BinTree', 'key, deep, left, right, papa')


    tree = None
    bee = BinTree(0,0,0,0,tree)
    vee = BinTree(0,0,bee,0,bee)

    zee = vee.left

    #zee.left = BinTree(0,0,0,0,tree)

    ADD_n(1)
    #ADD_n(2)
    #ADD_n(3)
    ADD_n(4)
    ADD_n(6)
    ADD_n(3)
    ADD_n(7)
    ADD_n(9)
    ADD_n(10)
    ADD_n(14)
    ADD_n(13)

    print("eee",tree)


    PRINTTREE() 

