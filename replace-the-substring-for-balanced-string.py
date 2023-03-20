class Solution:
    def balancedString(self, s: str) -> int:
        answer = len(s)
        left = 0
        right = 0
        count = Counter(s)

        n = len(s)/4
        dic = {}
        for key,val in count.items():
            if val > n:
                dic[key] = val - n
        if len(dic) == 0:
            return 0
        size = len(dic)

        while left < len(s):
            if s[left] in dic:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    size -= 1
            
            while size == 0:
                answer = min(answer,left-right+1)
                if s[right] in dic:
                    dic[s[right]] += 1
                    if dic[s[right]] == 1:
                        size += 1
                right += 1
            left += 1
        return answer