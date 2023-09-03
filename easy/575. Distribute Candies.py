class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        leng = int(len(candyType)/2)

        return min(int(len(candyType)/2), len(set(candyType)))


a = Solution()
a = a.distributeCandies([6,6,6,6])
print(a)
