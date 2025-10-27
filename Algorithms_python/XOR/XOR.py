#Дан массив A из n — 1 целых чисел, находящихся в интервале от 1 до n. 
#Все числа встречаются в нём ровно один раз, за исключением одного отсутствующего числа.
#Найти это отсутствующее число.

def find_missing(A,n):
    result = 0

    for num in range(n-1):
        result = result^A[num]

    for num in range(1,n+1):
        result = result^num

    return result 

def find_missing2(A, n):
  result = 0

  # Add all the values from 1 to n
  for value in range(1, n + 1):
    result += value

  # Subtract all values in the given array
  for value in A:
    result -= value

  return result

if __name__ == "__main__":
    print(find_missing([1,2,3,4,6],6))