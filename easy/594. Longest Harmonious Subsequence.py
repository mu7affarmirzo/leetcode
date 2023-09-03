import collections


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        count = collections.Counter(nums)

        for num, freq in count.items():
            if num + 1 in count:
                ans = max(ans, freq + count[num + 1])

        return ans

a = Solution()
a = a.findLHS([3,2,1])
print(a)