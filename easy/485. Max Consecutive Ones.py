class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_temp = 0
        temp = 0
        for i in nums:
            print('i', i)
            if i == 1:
                temp += 1
                # max_temp = temp
            else:
                if temp > max_temp:
                    max_temp = temp
                temp = 0
            if temp > max_temp:
                max_temp = temp
            print('m', max_temp)
            print('temp', temp)
            print()
        print(max_temp)
        return max_temp

a = Solution()
s = a.findMaxConsecutiveOnes([1,0,1,1,0,1])
# print(s)