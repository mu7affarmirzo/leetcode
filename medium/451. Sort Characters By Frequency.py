class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        b = sorted(list(set(s)))
        a = []
        for i in range(len(b)):
            if b[i] in s:
                a.append(b[i] * s.count(b[i]))
        c = sorted(a, key=len)
        return ("".join(c[::-1]))


a = Solution()
a = a.frequencySort('treee')
print(a)