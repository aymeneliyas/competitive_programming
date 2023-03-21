class Solution:
    def __init__(self):
        self.ans = []
    def backtrack(self,combination,idx,n,k):
        self.arr = [num for num in range(1,n + 1)]
        if len(combination) == k:
            self.ans.append(combination[:])
            return

        if idx > n:
            return 
        
        for i in range(idx,n):
            combination.append(self.arr[i])
            self.backtrack( combination,i+1,n,k)
            combination.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack([],0,n,k)
        return self.ans