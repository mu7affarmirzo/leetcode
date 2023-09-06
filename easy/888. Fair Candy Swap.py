class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        s = sum(aliceSizes + bobSizes)//2
        a = sum(aliceSizes)
        b = sum(bobSizes)
        print(s)


a = Solution()
a = a.fairCandySwap([1, 3], [2])
print(a)

