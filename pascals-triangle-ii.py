class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        
        arr = [1] * (rowIndex+1)
        ans = self.getRow(rowIndex-1)
        for i in range(1,len(arr)-1):
            arr[i] = ans[i-1] + ans[i]
        return arr