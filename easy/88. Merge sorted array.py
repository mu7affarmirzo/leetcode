class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n:
            nums1 = nums1[:m] + nums2[:n]
        nums1 = sorted(nums1)

        print(nums1)

s = Solution().merge([0], 1, [6], 1)
