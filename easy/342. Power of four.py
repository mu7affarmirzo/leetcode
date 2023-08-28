class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        print(n)
        if n == 0:
            return False
        if n == 1:
            return True
        if n//4 == 1 and n%4 == 0:
            print(n)
            return True
        elif n//4 == 1 and n%4 != 0:
            return False

        return self.isPowerOfFour(n/4)

a = Solution()
a = a.isPowerOfFour(1)
print(a)