class Solution:
    def rev(self,s,left,right):
        if left > right:
            return
        s[left],s[right] = s[right],s[left]
        self.rev(s,left+1,right-1)
        
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.rev(s,0,len(s)-1)
        return s