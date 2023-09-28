class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        l, r = 0, indexDiff
        if indexDiff > len(nums) - 1:
            return False
        while r <= len(nums) - 1:
            if abs(nums[l] - nums[r]) <= valueDiff:
                return True
            l += 1
            r += 1
        return False


a = Solution()
a = a.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3)
print(a)