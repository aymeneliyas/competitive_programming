class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n<0:
            x = 1/x
        n = abs(n)
        if n %2 == 0:
            ans = self.myPow(x*x,n//2)
            return ans
        if n %2 != 0:
            ans = x * self.myPow(x*x,n//2)
            return ans