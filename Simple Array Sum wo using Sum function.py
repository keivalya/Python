def SumArr(n,arr):
    sum = 0
    i = 0
    while i<n:
        sum = sum + arr[i]
        i = i+1
    return sum

arr1 = list(map(int, input().split()))
n1 = int(input())
print(SumArr(n1, arr1))