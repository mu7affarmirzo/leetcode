# class Solution(object):
#     def countDigitOne(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         m = n % 10
#         r = n
#         temp = n // 10
#
#         res = 0
#
#         def in_count(res, r, temp):
#             if 10 > r >= 1:
#                 return 10*temp + r
#             else:
#                 return res + in_count(res, r // 10, temp)
#         temp = in_count(res, r)
#         print(temp, 'temp')
#         res += temp
#
#         return res
#
#
# a = Solution()
# a = a.countDigitOne(1001)
# print(a)