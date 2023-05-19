import heapq
from collections import deque
from collections import defaultdict
n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))

for i in range(len(arr)):
    arr[i] = [arr[i],i+1]
heapq.heapify(arr)

graph = defaultdict(list)

for i in range(m):
    start,end = list(map(int,input().split()))
    graph[start].append(end)
    graph[end].append(start)

def bfs(node,visited):
    queue = deque([node])
    
    while queue:
        val = queue.popleft()
        for ver in graph[val]:
            if ver not in visited:
                queue.append(ver)
                visited.add(ver)


visited = set()
count = 0
for i in range(n):
    cost, idx = heapq.heappop(arr)
    if idx not in visited:
        count += cost
        bfs(idx,visited)

print(count) 


