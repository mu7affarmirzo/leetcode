class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        temp = len(s)
        if temp != 0 and len(s) == 0:
            return False
        if temp == 0 and len(t) != 0:
            return True
        print(temp, len(s))
        for i in range(len(t)):
            print(s[-temp], t[i])
            if t[i] == s[-temp]:

                temp -= 1
                if temp == 0:
                    return True
        return False


a = Solution()
a = a.isSubsequence('', 'ahbgdc')
print(a)