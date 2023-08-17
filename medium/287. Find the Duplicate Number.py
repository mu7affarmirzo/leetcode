class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int((sum(nums) - sum(set(nums)))/(len(nums)-len(set(nums))))

a = Solution()
a = a.findDuplicate([2,2,2,2,2,2,2,2])
print(a)

