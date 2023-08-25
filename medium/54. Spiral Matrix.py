class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []

        length = len(matrix)
        height = len(matrix[0])

        horizontal = [0, 0]
        vertical = [0, 0]





a = Solution()
a = a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]])

print('\n')
m =[[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
for i in m:
    for x in i:
        print(x, end=' ')
    print('\n')


