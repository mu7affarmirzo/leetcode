class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) > 1:
            digits = [int(x) for x in str(num)]
            num = sum(digits)

        return num

a = Solution()
a = a.addDigits(38)
#
# print([int(x) for x in str(integer)])