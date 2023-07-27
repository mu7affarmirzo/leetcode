
class Solution(object):
    def convertToTitle(self, n):
        """
        :type columnNumber: int
        :rtype: str
        """

        result = ''
        while n > 0:
            n -= 1
            result = chr(ord('A') + (n % 26)) + result
            n //= 26
        return result


a = Solution()
s = a.convertToTitle(52)
print(s)