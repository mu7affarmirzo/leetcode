class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n >= 12 and str(n) != str(n)[::-1]:
            return False

        for i in range(2, n-1):
            if not self.numberToBase(n, i):
                return False
        return True

    def numberToBase(self, n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b

        print(digits[::-1])
        return digits[::-1] == digits


a = Solution()
a = a.isStrictlyPalindromic(13)
print(a)