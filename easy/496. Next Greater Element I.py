class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        l_n2 = len(nums2)
        for i in nums1:
            ind = nums2.index(i)
            if ind+1 < l_n2:
                temp = False
                for j in range(ind+1, l_n2):
                    if nums2[j] > i:
                        res.append(nums2[j])
                        temp = True
                        break
                if not temp:
                    res.append(-1)
            else:
                res.append(-1)

        return res


a = Solution()
s = a.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7])
print(s)