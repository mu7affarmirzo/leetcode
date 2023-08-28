class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        a, b = 0, len(nums) - 1

        while a<b:
            if nums[a] + nums[b] == 0:
                return nums[b]
            elif nums[a] + nums[b] > 0:
                b -= 1
            else:
                a += 1
        return -1


a = Solution()
a = a.findMaxK([-1,2,-3,3, 5,4,6, -4])
print(a)