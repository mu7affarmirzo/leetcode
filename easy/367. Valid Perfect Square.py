class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(num//2+1):
            if i*i == num:
                print(i)
                return True
            elif i*i > num:
                return False
        return False


a = Solution()
a = a.isPerfectSquare(2000105819)
print(a)