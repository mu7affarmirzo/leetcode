from functools import reduce
from operator import xor


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zor = reduce(xor, nums)
        res = reduce(xor, filter(lambda i: i & (zor ^ (zor & (zor - 1))), nums))
        return [res, res ^ zor]


a = Solution()
s = a.singleNumber([1, 1, 2, 3, 4, 4])
