class Solution(object):
    def removeKdigits(self, num, k):
        if len(num) == k:
            return '0'
        stack = []
        for i in num:
            while k > 0 and stack and stack[-1] > i:
                k -= 1
                stack.pop()
            stack.append(i)
        return str(int(''.join(stack[:len(stack)-k])))


a = Solution()
a = a.removeKdigits('1432219', 3)
print(a)