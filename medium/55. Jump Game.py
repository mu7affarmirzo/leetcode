class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if nums[i] + i >= target:
                target = i
        return target == 0


a = Solution()
a = a.canJump([2,3,1,0,4])
print(a)