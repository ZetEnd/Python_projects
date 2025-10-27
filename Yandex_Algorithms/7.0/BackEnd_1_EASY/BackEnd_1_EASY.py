N = int(input())

arr = list(map(int, input().split()))
           
dictA = {}
           
num = arr[0]
maximum = 0
count = 1
num_rn = num
           
for i in range(1, len(arr)):
           #if arr[i] not in dictA.keys():
           #		dictA[arr[i]] = 
    if arr[i] == num and (arr[i] <= num_rn + 1 and arr[i] >= num_rn - 1):
        count += 1
        if maximum < count:
            maximum = count
        count = 1
        num_rn = arr[i]
    elif arr[i] <= num_rn + 1 and arr[i] >= num_rn - 1:
        count += 1
        num_rn = arr[i]

print(maximum)
           

