class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort() # sort the cookie sizes in non-decreasing order
        contentChildren = 0
        i = 0 # pointer to the current child's greed factor
        j = 0 # pointer to the current cookie size
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                contentChildren += 1
                i += 1
            j += 1
        return contentChildren