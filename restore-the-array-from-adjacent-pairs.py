class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)

        start = adjacentPairs[0][0]
        for idx, val in graph.items():
            if len(val) ==1:
                start = idx
                break
		
        ans=[]
        visited = set()
        def dfs(num):
            visited.add(num)
            for ver in graph[num]:
                if ver not in visited:
                    dfs(ver)
            ans.append(num) 
        dfs(start)
        return ans