# class Solution(object):
#     def maxEnvelopes(self, envelopes):
#         """
#         :type envelopes: List[List[int]]
#         :rtype: int
#         """
#         temp = []
#         w = []
#         h = []
#         for i in range(len(envelopes)):
#             temp.append(envelopes[i])
#             w.append(envelopes[i][0])
#             h.append(envelopes[i][1])
#             for j in range(i+1, len(envelopes)):
#                 if envelopes[j][0] in w or envelopes[j][1] in h:
#                     continue
#                 elif envelopes[j][0] > 1:
#                     pass
#
#         # for i in envelopes:
#         #     if temp == None:
#         #         temp.append(i)
#         #     else:
#         #         pass
#
#
#
#
# a = Solution()
# a = a.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])
# print(a)
#
x = [1,3]
res = 0
for i in x:
    res ^= i
    print(res)
print(res)
print(1^3)