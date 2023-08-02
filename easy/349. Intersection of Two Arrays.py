class Solution(object):
    def intersection(self, lst1, lst2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # return list(set(nums1) & set(nums2))
        # return set(nums1).intersection(nums2)
        temp = set(lst2)
        lst3 = [value for value in lst1 if value in temp]
        return set(lst3)