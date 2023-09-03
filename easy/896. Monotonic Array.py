class Solution:
    def isMonotonic(self, nums):
        return nums == sorted(nums) or nums == sorted(nums)[::-1]


a = Solution()
a = a.isMonotonic([1,2,2,3])
print(a)