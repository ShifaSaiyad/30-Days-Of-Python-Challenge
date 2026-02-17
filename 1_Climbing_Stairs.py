class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
    
        first =1
        second=2

        for i in range(3,n+1):
            third = first + second
            first =second
            second=third
        return second



        '''for i in range(1,n):
            while(n-i >0):
                print(n,i)
                i+=1'''
        