# class Solution(object):
#     def canSeePersonsCount(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: List[int]
#         """
#         res = [] * len(heights)
#         stack = [0]
#
#         for i, height in enumerate(heights):
#             temp = 0
#
#             while stack and heights[i] > stack[-1]:
#                 temp += 1
#             res.append(temp)
#
#         return res
#
#
# a = Solution()
# a = a.canSeePersonsCount([3, 1, 4, 2, 5])
# print(a)


words= ["alice","bob","charlie"]
s='abc'
temp = ''
for i in range(len(words)):
    if s[i] == words[i][0]:
        continue
    else:
        print(False)
print(True)
