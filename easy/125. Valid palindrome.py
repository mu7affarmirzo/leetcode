import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new_str = re.sub(r'[\W_]', '', s)
        print(new_str)
        print(new_str[::-1])
        if new_str[::-1] == new_str:
            return True
        else:
            return False

a = Solution()
s = a.isPalindrome('A man, a plan, a canal: Panama')
