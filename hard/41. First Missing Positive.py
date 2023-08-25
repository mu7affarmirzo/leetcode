class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        nums = set(nums)
        while k in nums:
            k += 1
        return k


a = Solution()
a = a.firstMissingPositive([7,8,9,11,12])
print(a)