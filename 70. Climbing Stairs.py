class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        x,y=1,2
        for i in range(3,n+1):        # int  not use len(n)
            x,y=y,x+y
        return y