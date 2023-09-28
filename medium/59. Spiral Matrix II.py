class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for x in range(n)] for k in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        temp = 1
        while top <= bottom and left <= right:
            # Traverse right
            for i in range(left, right + 1):
                matrix[top][i] = temp
                temp += 1
            top += 1
            # Traverse down
            for i in range(top, bottom + 1):
                matrix[i][right] = temp
                temp += 1
            right -= 1
            # Traverse left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = temp
                    temp += 1
                bottom -= 1
            # Traverse up
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = temp
                    temp += 1
                left += 1
        return matrix

a = Solution()
a = a.generateMatrix(3)
print(a)
