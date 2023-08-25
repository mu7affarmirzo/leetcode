class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        a, b = 0, len(nums) - 1
        # [1,2,3,5]
        while a < b:
            print(a,b)
            if nums[a] % 2 == 0:
                a += 1
            elif nums[a] % 2 != 0 and nums[b] % 2 == 0:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
            else:
                b -= 1
        return nums

a = Solution()
a = a.sortArrayByParity([0])
print(a)



        # for x in nums:
        #     pass