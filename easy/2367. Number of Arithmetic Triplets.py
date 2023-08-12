# class Solution(object):
#     def arithmeticTriplets(self, nums, diff):
#         """
#         :type nums: List[int]
#         :type diff: int
#         :rtype: int
#         """
#         vis = set(nums)
#         return sum(x + diff in vis and x + diff * 2 in vis for x in nums)
#
#
# a = Solution()
# s = a.arithmeticTriplets([0,1,4,6,7,10], 3)
# print(s)


if '-' in 'X--':
    print('good')