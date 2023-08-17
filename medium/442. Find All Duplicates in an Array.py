class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums:
            nums[abs(n) - 1] = -nums[abs(n) - 1]
            if nums[abs(n) - 1] > 0:
                ans.append(abs(n))
        return ans

a = Solution()
a = a.findDuplicates([1,1,1,3,4,3,4,2])
print(a)

a = [1,1,1,3,4,3,4,2]
a.remove(1)
print(a)

