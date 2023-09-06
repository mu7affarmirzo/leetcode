class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        rev = nums[::-1]
        l = len(nums)
        for i in range(l):
            if nums[i] == target:
                res[0] = i
                break

        for i in range(l):
            print(i)
            if rev[i] == target:
                res[1] = l - i - 1
                break
        return res



a = Solution()
a = a.searchRange([1], 1)
print(a)