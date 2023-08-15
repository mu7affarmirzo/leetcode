class Solution(object):
    def diStringMatch(self, S):
        """
        :type s: str
        :rtype: List[int]
        """
        l, r, arr = 0, len(S), []
        for s in S:
            arr.append(l if s == "I" else r)
            l, r = l + (s == "I"), r - (s == "D")
        return arr + [l]


a = Solution()
a = a.diStringMatch('IIDD')
print(a)

