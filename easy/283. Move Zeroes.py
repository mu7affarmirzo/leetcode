class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            print(nums)
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

        return nums


a = Solution()
s = a.moveZeroes([-58305,-22022,0,0,0,0,0,-76070,42820,48119,0,95708,-91393,60044,0,-34562,0,-88974])
print(s)