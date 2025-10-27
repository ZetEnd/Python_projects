# Куча - бинарное дерево на массиве
def push_heap(heap_list,x):
    heap_list.append(x) # add an element x
    pos = len(heap_list) - 1 # number of last element for proseivat up
    #print(" x is ", x)
    # heap_list - просто массив
    while pos > 0 and heap_list[pos] < heap_list[(pos-1)//2]:
        heap_list[pos], heap_list[(pos - 1)//2] =\
            heap_list[(pos - 1)//2],heap_list[pos]
        pos = (pos - 1)//2
   #print(" xlst pos is ", pos)


def pop_heap(heap_list):
    ans = heap_list[0]
    heap_list[0] = heap_list[-1]
    pos = 0
    while pos*2 + 2 < len(heap_list):
        min_son_index = pos*2+1
        if heap_list[pos*2+2] < heap_list[min_son_index]:
            min_son_index = pos*2+2
        if heap_list[pos] > heap_list[min_son_index]:
            heap_list[pos], heap_list[min_son_index] =\
                heap_list[min_son_index], heap_list[pos]

            pos = min_son_index
        else:
            break;

    heap_list.pop() #

    return ans

if __name__ == "__main__":

    hl = []
    N = int(input())

    for i in range(N):
        push_heap(hl, int(input()))

    n = 0
    step = 0
    for i in hl:
        print(i, " ",end='')
        n+=1
        if n == pow(2,step):
            print("\n")
            step +=1
            n = 0

    print("\n")

    #for i in range(len(hl)):
    #    print(i, " ", hl[i],end='')
