class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(set(nums))
        print(3*sum(set(nums)))
        print(sum(nums))
        return int((3*sum(set(nums)) - sum(nums))/2)
        # [1,1,1, 3, 3, 3, 4]
        # {1, 3, 4] => {1,1, 3, 3, 4, 4, 4]

a = Solution()
s = a.singleNumber([2,2,3,2])
print(s)