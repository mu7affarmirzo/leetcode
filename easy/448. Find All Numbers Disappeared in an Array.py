class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst1 = len(nums)
        set_nums = set(nums)
        print(lst1)

        lst3 = [value for value in range(1, lst1+1) if value not in set_nums]
        return lst3


a = Solution()
s = a.findDisappearedNumbers([1,1])
print(s)