# class Solution(object):
#     def deleteGreatestValue(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         res = 0
#         while len(grid) > 0:
#             temp = [0]
#             for i in range(len(grid)):
#                 if len(grid[i]) > 0:
#                     temp.append(max(grid[i]))
#                     grid[i].remove(max(grid[i]))
#                 else:
#                     grid.remove(grid[i])
#             res += max(temp)
#         return res
#
#
# a = Solution()
# a = a.deleteGreatestValue([[1,2,4],[3,3,1]])
# print(a)

x = {'i': 1}
print('i' in x)