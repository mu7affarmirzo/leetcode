class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        n, m = len(nums1), len(nums2)

        for i in range(n):
            for j in range(m):
                pass


a = Solution()
a = a.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]])
print(a)