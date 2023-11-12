class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [s[0]]
        for i in range(1, len(s)):
            if stack and stack[-1] == s[i]:
                stack.append(s[i])
            elif stack and (stack[-1].lower() == s[i] or stack[-1].upper() == s[i]):
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)


a = Solution()
a = a.makeGood('abBAcC')
print(a)