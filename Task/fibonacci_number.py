class Solution(object):
    def fib(self,n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1
        for n in range(2,n+1):
            sum = a + b 
            a = b
            b = sum
        return b

sol = Solution()
print(sol.fib(4))
print(sol.fib(3))
print(sol.fib(2))
