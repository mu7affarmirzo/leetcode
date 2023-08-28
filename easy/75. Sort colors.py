class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        col = [0] * len(nums)
        zero = 0
        one = len(nums) // 3
        two = one * 2
        for i in nums:
            if i == 0:
                col[zero] = i
                zero += 1
            elif i == 1:
                col[one] = i
                one += 1
            else:
                col[two] = i
                two += 1
        return col

a= Solution()
a = a.sortColors([2,0,2,1,1,0])
print(a)