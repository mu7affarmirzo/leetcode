class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums) - 1
        res = 1
        max_jump = nums[0]
        left, right = 0, nums[0]
        while left <= l:
            if nums[left] + left == l:
                return res
            else:
                if max(nums[left:max_jump+left+1]) > max_jump:
                    print(max(nums[left:max_jump+left+1]), max_jump, nums[max(nums[left:max_jump+left+1])])
                    max_jump = nums[max(nums[left:max_jump+left+1])] + left
                res += 1
                left = max_jump
        return res



a = Solution()
a = a.jump([2,3,0,1,4, 1,1,1,2,1,5,3,4,2,0,3,0])
print(a)