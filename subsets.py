class Solution:
    def __init__(self):
        self.ans = []
    def backtrack(self,combination,idx,n,nums):
        

        if idx > n:
            return 
        
        self.ans.append(combination[:])
        
        for i in range(idx,n):
            combination.append(nums[i])
            self.backtrack( combination,i+1,n,nums)
            combination.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack([],0,len(nums),nums)
        return self.ans