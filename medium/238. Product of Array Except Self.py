class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = 1, 1
        len_n = len(nums)

        if len_n == 0 or nums is None:
            return nums
        ans = [1] * len_n

        for i in range(0, len_n):
            ans[i] *= l
            l *= nums[i]
            ans[len_n -i - 1] *= r
            r *= nums[len_n - i - 1]
        print(ans)
        return ans

a = Solution()
a = a.productExceptSelf([-1,1,0,-3,3])

m = [1,2,4]
print(m.count(0))