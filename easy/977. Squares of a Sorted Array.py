class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        nums = sorted([abs(x) for x in nums])
        print(nums)
        for i in nums:
            res.append(i*i)
        return res

a = Solution()
a = a.sortedSquares([-4,-1,0,3,10])
print(a)