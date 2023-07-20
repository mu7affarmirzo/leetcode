class Solution (object):
    def generateParenthesis (self, n):
        ans = []
        def gen(o, c, s):
            if o > c:
                return
            if o == 0 and c == 0:
                ans.append(s)
                return
            if o == 0:
                gen(o, c-1, s+')')
            else:
                gen(0-1, c, s+'(')
                gen(o, c-1, s+')')
        gen(n, n, '')
        return ans

a = Solution()
s = a.generateParenthesis(3)
print(s)