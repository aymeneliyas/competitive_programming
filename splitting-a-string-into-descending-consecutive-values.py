class Solution:
    def backtrack(self,idx,arr,s):
        if idx >= len(s):
            return len(arr) >= 2

        for i in range(idx,len(s)):
            value = int(s[idx:i+1])
            if not arr or arr[-1] - value == 1:
                arr.append(value)
                ans = self.backtrack(i+1,arr[:],s)
                arr.pop()
                if ans:
                    return True
                
        return False
    def splitString(self, s: str) -> bool:
        return self.backtrack(0,[],s)