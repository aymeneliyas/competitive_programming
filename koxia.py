import heapq
n = int(input())
for _ in range(n):
    n,m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    heapq.heapify(arr)
    op = list(map(int,input().split()))
    
    for i in range(m):
        heapq.heappop(arr)
        heapq.heappush(,oparr[i])
    print(sum(arr))

