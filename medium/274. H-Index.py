class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] == i+1:
                return i+1
        return 1 if citations[-1] == 1 else 0


a = Solution()
a = a.hIndex([11,15])
print(a)