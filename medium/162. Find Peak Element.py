class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        mid = (left+right) // 2
        while left <= right:
            if nums[mid] > nums[mid+1] and nums[mid]:
                left = mid + 1
        
        index = nums.index(max(nums))
        return index


a = Solution()
a = a.findPeakElement([1,2,3,1])
print(a)