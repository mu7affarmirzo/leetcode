class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        prev = nums[0]
        res = []
        for j in range(len(nums)):
            pass
        for i in nums:
            print(f"prev: {prev}\ni: {i}")
            if (i - prev) <= 1:
                prev = i
            else:
                print('------')
                res[-1] = res[-1] + "->" + str(prev)
                print(res[-1])
                res.append(str(i))
                print(res)
                prev = i
        return res

a = Solution()
s = a.summaryRanges([0,2,3,4,6,8,9])
print(s)
