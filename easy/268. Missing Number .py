class Solution(object):
    def missingNumber(self, nums):
        max_len = len(nums)
        sum_a_p = (max_len + 1) * (max_len) / 2
        return sum_a_p - sum(nums)
