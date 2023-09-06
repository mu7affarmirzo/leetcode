class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        index = 2
        while True:
            if (index + 1)*index//2 > n:
                return index - 1


a = Solution()
a = a.arrangeCoins(5)
print(a)