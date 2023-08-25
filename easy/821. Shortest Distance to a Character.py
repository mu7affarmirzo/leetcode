# # class Solution(object):
# #     def shortestToChar(self, s, c):
# #         """
# #         :type s: str
# #         :type c: str
# #         :rtype: List[int]
# #         """
# #         res = []
# #         for i in range(len(s)):
# #             a, b = 0, len(s) - 1
# #             while a <= i <= b:
# #                 print(i, a, b)
# #                 print(s[a], s[b], c)
# #                 temp = len(s)-1
# #                 if s[a] != c:
# #                     a += 1
# #                 elif s[b] != c:
# #                     b -= 1
# #                 elif s[a] == c:
# #                     print('----', temp, abs(a-i))
# #                     if temp > abs(a-i) > 0:
# #                         temp = abs(a-i)
# #                     elif abs(a-1) == 0:
# #                         res.append(0)
# #                         break
# #                     a += 1
# #                 elif s[b] == c:
# #                     if temp > abs(a-i) > 0:
# #                         temp = abs(a-i)
# #                     elif abs(a-1) == 0:
# #                         res.append(0)
# #                         break
# #                     b -= 1
# #                 else:
# #                     a += 1
# #                     b -= 1
# #             res.append(temp)
# #
# # a = Solution()
# # a = a.shortestToChar('strong', 's')
# # print(a)
# class A:
#     def __init__(self):
#         self.state = 4
#
# cheque = A()
#
# message_mapping = {
#         "Created!": 0,
#         "cancelled": 21,
#         "returned": 5,
#         "waiting": 30,
#         "Successful": 4
#     }
#
# message = message_mapping.get(cheque.state)
# print(message)

print(set('hello'))