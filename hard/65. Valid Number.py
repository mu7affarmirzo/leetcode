class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        try:
            s = float(s)
            return True
        except:
            return False

        # return s


a = Solution()
a = a.isNumber('e3')
print(a)

# x = '123123eeee2'
# print(x.replace('e', '', 1))