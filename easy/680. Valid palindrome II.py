class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s[::-1] == s:
            return True
        a, b = 0, len(s) - 1
        while a < b:
            if s[a] == s[b]:
                a += 1
                b -= 1
            else:
                temp = s[0:a] + s[a + 1:]
                if temp == temp[::-1]:
                    return True
                else:
                    temp = s[a:b]
                    print(temp)
                    if temp == temp[::-1]:
                        return True
                    else:
                        a += 1
                        b -= 1
        return False


a = Solution()
a = a.validPalindrome('cxcaac')
print(a)