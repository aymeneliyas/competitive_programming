class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.ans = float("+inf")
        self.arr = [0] * k
        
        if len(cookies) == k:
            return max(cookies)
        
        self.backTracking(cookies,0, k)
        
        return self.ans
    
    def backTracking(self, cookies , idx, k):
        if idx >= len(cookies):
            self.ans = min(self.ans, max(self.arr))
            return
        
        if self.ans < max(self.arr):
            return 
        
        for i in range(k):
            self.arr[i] += cookies[idx]
            self.backTracking(cookies,idx + 1, k)
            self.arr[i] -= cookies[idx]
        return