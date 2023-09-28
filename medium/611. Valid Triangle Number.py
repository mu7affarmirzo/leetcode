class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in nums:
            a, b = 0, len(nums) - 1
            while a<=b:
                if i < b:
                    pass
                