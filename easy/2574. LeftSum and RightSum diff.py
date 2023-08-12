class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        l_sum = []
        r_sum = []

        for i in range(len(nums)):
            if i == 0:
                l_sum.append(0)
                r_sum.append(0)
            else:
                l_sum.append(l_sum[i - 1] + nums[i - 1])
                r_sum.append(r_sum[i - 1] + nums[-i])

        r_sum = r_sum[::-1]

        for i in range(len(nums)):
            res.append(abs(l_sum[i]-r_sum[i]))

        return res

a = Solution()
s = a.leftRightDifference([10,4,8,3])
