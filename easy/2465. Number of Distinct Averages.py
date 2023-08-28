class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        # nums = sorted(nums)
        a, b = 0, len(nums) - 1
        while a < b:
            res.append((min(nums) + max(nums)) / 2)
            nums.remove(min(nums))
            nums.remove(max(nums))
            a += 1
            b -= 1

        print(res)
        return len(set(res))


a = Solution()
a = a.distinctAverages([9,5,7,8,7,9,8,2,0,7])
print(a)