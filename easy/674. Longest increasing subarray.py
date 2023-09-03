class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        if len(nums)==1 or len(set(nums)) == 1:
            return 1
        prev = nums[0]
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                print('----', temp)
                if res < len(temp):
                    res = len(temp)
                temp = [nums[i]]
            else:
                temp.append(nums[i])
            prev = nums[i]
        print(temp)
        if res < len(temp):
            res = len(temp)
        return res


a = Solution()
a = a.findLengthOfLCIS([1,3,5,4,2,3,4,5])
print(a)