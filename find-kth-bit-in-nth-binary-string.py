class Solution:
    def getWord(self,n,k):
        if n == 1:
            return "0"
        
        ans = self.getWord(n-1,k)
        arr = []
        for ch in ans:
            if ch == "0":
                arr.append("1")
            else:
                arr.append("0")
        
        
        q = "".join(arr[::-1])
        
        return ans + "1" + q
    
    def findKthBit(self, n: int, k: int) -> str:
        ans = self.getWord(n,k)
        return ans[k-1]