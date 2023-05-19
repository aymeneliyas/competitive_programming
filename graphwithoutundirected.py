import sys
from collections import deque
from collections import defaultdict
n,m = list(map(int,input().split()))
graph = defaultdict(list)
queue = deque()

def bfs(node,graph):
    queue.append([node,1])
    color_dict[node] = 1

    while queue:
        val,color = queue.pop()
        for ver in graph[val]:
            if ver in color_dict:
                if color_dict[ver] == color:
                    return False
            else:
                queue.append([ver,1-color])
                color_dict[ver] = 1-color
    return True

edges = []
for i in range(m):
    arr = list(map(int,input().split()))
    edges.append(arr)
    graph[arr[0]].append(arr[1])
    graph[arr[1]].append(arr[0])

color_dict = {}
for i in range(1,n+1):
    if i not in color_dict:
        if not bfs(i,graph):
            print("NO")
            sys.exit()

print("YES")
ans = []
for a,b in edges:
    if color_dict[a]- color_dict[b] == 1:
        ans.append("1")
    if color_dict[a] - color_dict[b] == -1:
        ans.append("0")

print("".join(ans))





