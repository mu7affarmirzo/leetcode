class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in s:
            t = t.replace(i, '', 1)
        return t


a = Solution()
a = a.findTheDifference('abcd', 'abcde')
print(a)