class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if min(nums) > 0 or max(nums) < 0:
            return len(nums)

        # n, p = 0, 0
        # for i in nums:
        #     if i > 0:
        #         p += 1
        #     elif i < 0:
        #         n += 1
        # print(p, n)
        # return max(p, n)
        # a, b = 0, len(nums) -1 
        # mid = 0


a = Solution()
a = a.maximumCount([-2,-1,-1,1,2,3])
print(a)