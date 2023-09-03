class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = s + s
        print(t, t[1:-1])
        return (s in t[1:-1])


a = Solution()
a = a.repeatedSubstringPattern('abaababaab')
print(a)

