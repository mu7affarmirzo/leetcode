class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        prev = 0

        res = []
        has_prev = False
        # for j in range(len(nums)):

        for i in nums:
            print(f"prev: {prev}\ni: {i}")
            if (i - prev) == 1:
                prev = i
                has_prev = True
            else:
                print('------')
                if has_prev:
                    res[-1] = res[-1] + "->" + str(prev)
                    has_prev = False
                print(res[-1])
                res.append(str(i))
                print(res)
                prev = i
        return res

a = Solution()
s = a.summaryRanges([0,2,3,4,6,8,9])
print(s)
