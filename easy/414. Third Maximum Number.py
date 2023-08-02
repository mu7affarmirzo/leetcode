class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = sorted(set(nums))
        print(set_nums)
        len_n = len(set_nums)
        if len_n < 3:
            return max(set_nums)
        elif len_n == 3:
            return min(set_nums)
        else:
            return set_nums[-3]

        # set_nums = sorted(set(nums))
        # if len(set_nums) > 2:
        #     return set_nums[-3]
        # return set_nums[-1]


a = Solution()
s = a.thirdMax([3,2,1,2,3,2,5,4,3,5,3,6,7])
print(s)