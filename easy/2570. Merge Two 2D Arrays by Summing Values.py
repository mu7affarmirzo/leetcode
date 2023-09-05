class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        m = {}

        for i in nums1:
            m[i[0]] = i[1]

        for i in nums2:
            if i[0] in m:
                m[i[0]] += i[1]
            else:
                m[i[0]] = i[1]

        for i, v in m.items():
            res.append([i, v])

        return sorted(res)


a = Solution()
a = a.mergeArrays([[1,2],[2,3],[4,5], [5,1]], [[1,4],[3,2],[4,1]])
print(a)