class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return nums

        prev = nums[0]
        temp = 1
        res = 0
        a, b = 1, len(nums)-1
        while a < b:
            if nums[a] == prev and temp < 2:
                temp += 1
                a += 1
            elif nums[a] == prev and temp == 2:
                del nums[a]
                nums.append('_')
                res += 1
                b -= 1
            else:
                a += 1
                temp = 1
                prev = nums[a]

        return len(nums)-res


a = Solution()
a = a.removeDuplicates([1,1])
print(a)

