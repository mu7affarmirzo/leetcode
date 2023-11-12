class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num1 = ''
        num2 = ''
        nums = sorted([int(x) for x in str(num)])
        for i in range(len(nums)):
            if i % 2 == 0:
                num1 += str(nums[i])
            else:
                num2 += str(nums[i])

        return int(num1) + int(num2)

a = Solution()
a = a.splitNum(4325)
print(a)