import heapq
n = int(input())
for i in range(n):
    m = int(input())
    arr = list(map(int,input().split()))

    for i in range(m):
        arr[i] = [-arr[i],i+1]


    heapq.heapify(arr)
    ans = []
    while len(arr) > 1:
        fir,idx1 = heapq.heappop(arr)
        sec,idx2 = heapq.heappop(arr)
        
        val1 = abs(fir)
        val2 = abs(sec)
        if val1 and val2:
            ans.append([idx2,idx1])
            val1 -= 1
            val2 -= 1

            if val1:
                heapq.heappush(arr,[-val1,idx1])
            if val2:
                heapq.heappush(arr,[-val2,idx2])
        
        elif val1 and not val2:
            heapq.heappush(arr,[-val1,idx1])
        elif val2 and not val1:
            heapq.heappush(arr,[-val2,idx2])
    print(len(ans))
    if ans:
        ans.sort()
        for val in ans:
            val.sort()
            print(val[0],val[1])