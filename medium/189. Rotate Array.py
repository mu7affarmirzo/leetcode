class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        print(nums[-k:], nums[:-k])
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
        print(nums)


a= Solution()
a = a.rotate([1,2,3,4,5,7,5,4], 1)
print(a)