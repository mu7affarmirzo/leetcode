class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        res = []
        for i, v in enumerate(s):
            temp = len(s)
            for j, k in enumerate(s):
                if s[j] == c:
                    if temp > abs(j-i):
                        temp = abs(j-i)
            if s[i] == c:
                res.append(0)
            else:
                res.append(temp)

        return res

a = Solution()
a = a.shortestToChar('aaab', 'b')
print(a)
