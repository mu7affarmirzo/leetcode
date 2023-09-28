class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < k:
            if nums[i] < 0:
                nums[i] *= -1
                i += 1
            elif nums[i] == 0:
                return sum(nums)
            elif nums[i] > 0 and (k-i-1)%2 == 0:
                print('here')
                nums[i] *= -1
                return sum(nums)
            else:
                print('there')
                nums[i] *= -1
                return sum(nums)
        return sum(nums)


a = Solution()
a = a.largestSumAfterKNegations([4,2,3], 1)
print(a)