def bin_search(arr,l,r,x):

    while l < r:
        n = (l+r) // 2 
        if arr[n] < x:
            l = n+1
        elif arr[n] == x:
            return n
        else:
            r = n 

    return l

def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r-l) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binary_search(arr,l, mid-1,x)

        if arr[mid] < x:
            return binary_search(arr,mid+1,r,x)
    else:
        return -1

if __name__ == "__main__":
    arr = [0,1,2,3,4,5]
    arr = [ 2, 3, 4, 10, 40 ]
    l = 0
    r = len(arr)-1
    x = 4
    print(bin_search(arr, l, r, x))
    result = binary_search(arr, 0, len(arr)-1, x)
    print(result)
