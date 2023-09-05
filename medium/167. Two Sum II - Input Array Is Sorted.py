class Solution:
    def twoSum(self, nums, target):
        a, b = 0, len(nums) - 1
        temp = []
        while a<b:
            if nums[a] + nums[b] > target:
                b -= 1
            elif nums[a] + nums[b] < target:
                a += 1
            elif nums[a] + nums[b] == target:
                return [a+1, b+1]
        return []


a = Solution()
a = a.twoSum([1,2,3,5], 5)
print(a)