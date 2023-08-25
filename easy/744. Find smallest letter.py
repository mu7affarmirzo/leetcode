class Solution(object):
    def nextGreatestLetter(self, nums, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        res = nums[0]
        for i in range(len(nums)):
            print(min(nums[i:]), target, min(nums[i:]) > target)
            if min(nums[i:]) > target:
                return min(nums[i:])

        return nums[0]

a = Solution()
a = a.nextGreatestLetter(["c","f","j"], 'g')
print(a)
print('g' < 'j')

