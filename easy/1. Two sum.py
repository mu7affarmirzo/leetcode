class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(nums) - 1
        # temp = []
        while i < j:
            print(i, j)
            temp = nums[i] + nums[j]
            print(temp, target)
            if temp == target:
                return [i, j]
            elif temp > target:
                i += 1
            elif temp < target:
                j -= 1
        return []


a = Solution()
s = a.twoSum([3,2,4],6)
print(s)