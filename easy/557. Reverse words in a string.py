# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         s = s.split()
#         res = ''
#         for w in s:
#             temp = list(w)
#             i, j = 0, len(w) - 1
#             while i < j:
#                 temp[i], temp[j] = w[j], w[i]
#                 i += 1
#                 j -= 1
#             x = ''.join(temp)
#             if res:
#                 res = res + ' ' + x
#             else:
#                 res += x
#
#         return res
#
# a = Solution()
# s = a.reverseWords("Let's take LeetCode contest")
# print(s)

x = 1

x ^= 1

print(x)
