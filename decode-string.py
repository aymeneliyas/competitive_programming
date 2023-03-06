class Solution:
    def findRec(self,left,right,s):
        if s[left] in "0123456789" and s[right] == "]":
            idx = -1
            opening = 0
            for i in range(left,right+1):
                if opening > 1:
                    break
                if s[i] == "[":
                    opening += 1
                if s[i] == "[" and idx == -1:
                    idx = i
            if opening == 1 :
                
                val = s[idx+1 : right] * int(s[left:idx])
                return val

        arr = []
        count = 0
        while left <= right:
            if not s[left] in "0123456789":
                arr.append(s[left])
                left += 1         
            else:
                opening = 0
                closing = 0
                idx = -1
                temp = left
                while True:
                    if s[left] == "[":
                        opening += 1
                    if s[left] == "[" and idx == -1:
                        idx = left
                    elif s[left] == "]":
                        closing += 1
                    if closing > 0 and closing == opening:
                        break
                    if left >= right:
                        break 
                    left += 1
                
                ans = self.findRec(idx+1,left-1,s)
                res = ans * int(s[temp:idx])
                arr.append(res)
                left += 1

             
        return "".join(arr)    




    def decodeString(self, s: str) -> str:
        """
        3[a,  2[bc

        3[a2[c , " "


        """
        if s in "0123456789":
            return ""
        return self.findRec(0,len(s)-1,s)