class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        l, h = 0, 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j-i >= 0 and matrix[i][j] != matrix[0][j - i] or i-j >= 0 and matrix[i][j] != matrix[i - j][0]:
                    return False
            return True


a = Solution()
a = a.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
print(a)
