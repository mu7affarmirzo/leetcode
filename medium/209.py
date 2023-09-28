class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        if target in nums:
            return 1
        if sum(nums) < target:
            return 0
        elif sum(nums) == target:
            return len(nums)
        temp = []
        for i in range(len(nums)-1, 1, -1):
            print(temp, sum(temp), nums[i], nums[i-1], '-----')
            temp.append(nums[i])
            if sum(temp) + nums[i-1] >= target:
                print('FOUND', temp)
                return len(temp) + 1
            else:
                print(temp,'-0-', i)
                temp.append(nums[i-1])
                print(temp, '-0-', i)
        return len(temp)


a = Solution()
a = a.minSubArrayLen(11, [1,2,3,4,5])
print(a)

for i in range(10):
    print(i)
    i += 2


print(''.join([1,2,3]))