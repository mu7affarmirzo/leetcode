class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n // 3)%2==0 and n % 3 > 0:
            return True
        else: return False


a = Solution()
a = a.canWinNim(15)
print(a)