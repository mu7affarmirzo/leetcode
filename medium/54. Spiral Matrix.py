# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         if not matrix: return []
#
#         length = len(matrix)
#         height = len(matrix[0])
#
#         vertical_temp = 0
#         horizontal_temp = 0
#
#         vertical_index = 0
#         horizontal_index = height-1
#
#         for i in range(vertical_temp):
#             print(matrix[vertical_index][i], end='->')
#             horizontal_temp = i
#
#         for i in range(1, height):
#             print(matrix[i][vertical_index-1])
#             vertical_temp = i
#
#         for i in range()
#         # a, o_index = 0, len(matrix)-1
#         # b = len(matrix[0])-1
#         # reverse = 0
#         #
#         # print(a, b, o_index)
#         # while a <= o_index:
#         #     for i in range(len(matrix[0])-a):
#         #         print(matrix[a][i], end='->')
#         #         reverse = i
#         #     a += 1
#         #
#         #     # ---------
#         #     for k in range(a, o_index):
#         #         print(matrix[k][reverse], end='->')
#         #     # ---------
#         #
#         #     if a < o_index:
#         #         for j in range(b, -1, -1):
#         #             print(matrix[o_index][j], end='->')
#         #             reverse = j
#         #         for k in range(o_index-1, len(matrix[0])-a-2, -1):
#         #             print(matrix[k][reverse], end='->')
#         #         # ---------
#         #         b -= 1
#         #         o_index -= 1
#         #         # ---------
#         #
#         # print('\n', a, b)
#
# ma = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
# a = Solution()
# a = a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]])
#
#
# print('\n\n')
# for i in ma:
#
#     for j in i:
#         print(j, end='->')
#     print('\n')

a=[[]]*5
print(a[4])