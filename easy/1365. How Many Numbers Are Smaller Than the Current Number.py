class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            temp = 0
            for j in nums:
                if i > j:
                    temp += 1
            res.append(temp)
        return res

a = Solution()
s = a.smallerNumbersThanCurrent([8,1,2,2,3])
print(s)

