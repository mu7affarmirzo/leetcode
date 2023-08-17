class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # m = len(matrix)
        # n = len(matrix[0])
        # fm = fn = 1
        # for i in range(m):
        #     if matrix[i][0] == 0:
        #         fm = 0
        #         break
        # for i in range(n):
        #     if matrix[0][i] == 0:
        #         fn = 0
        #         break
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if matrix[i][j] == 0:
        #             matrix[i][0] = matrix[0][j] = 0
        #
        # for i in range(1, m):
        #     if matrix[i][0] == 0:
        #         for j in range(1, n):
        #             matrix[i][j] = 0
        # for j in range(1, n):
        #     if matrix[0][j] == 0:
        #         for i in range(1, m):
        #             matrix[i][j] = 0
        #
        # if fm == 0:
        #     for i in range(m):
        #         matrix[i][0] = 0
        # if fn == 0:
        #     for i in range(n):
        #         matrix[0][i] = 0

        m, n = len(matrix), len(matrix[0])
        tmp = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    tmp.append([i, j])

        for r, c in tmp:
            for i in range(n):
                matrix[r][i] = 0
            for j in range(m):
                matrix[j][c] = 0
        return matrix

a = Solution()
a = a.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
print(a)
#
def set_column_to_zero(matrix, m):
    for row in matrix:
        row[m] = 0
    return matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
column_to_zero = 1  # Column index to set to zero
result = set_column_to_zero(matrix, column_to_zero)
print(result)