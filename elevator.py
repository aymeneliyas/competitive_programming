n = int(input())
for i in range(n):
    arr = list(map(int,input().split()))
    num1 = 4 * arr[0]
    num2 = ((4 - (4-arr[2])) * arr[1]) + (4 * arr[1])
    num3 = (arr[2] * arr[0]) + (4 - arr[2]) * arr[1]
    
    arr = []
    arr.append(num1)
    arr.append(num2)
    arr.append(num3)
    print(min(arr))
