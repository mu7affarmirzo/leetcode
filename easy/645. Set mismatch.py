class Solution:
    def findErrorNums(self, nums):
        n = sum(nums)-sum(set(nums))
        s = (len(nums)/2) * (1 + len(nums))
        return [n, int(s-sum(set(nums)))]

a = Solution()
a = a.findErrorNums([2,2])
print(a)

print(max([1.2, 1.75]))