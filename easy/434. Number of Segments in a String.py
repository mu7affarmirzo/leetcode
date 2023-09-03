class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        print(s.split(' '))
        return len(s.split(' '))

a = Solution()
a = a.countSegments("             ")
print(a)