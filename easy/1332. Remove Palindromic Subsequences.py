class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 1 if s[::-1] == s else 2


a = Solution()
s = a.removePalindromeSub("ababb")
print(s)
