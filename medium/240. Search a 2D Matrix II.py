class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        top, bottom = 0, len(matrix) - 1
        up_mid = (top + bottom)//2
        left, right = 0, len(matrix[0]) - 1
        down_mid = (left + right)//2

        while top <= bottom:
            print('----', top, up_mid, bottom)
            if matrix[up_mid][0] == target:
                return True
            elif matrix[up_mid][0] > target:
                bottom = up_mid - 1
                up_mid = (top + bottom) // 2

            while left <= right:
                print(top, '==========', left, down_mid, right, matrix[top][down_mid])
                if matrix[top][down_mid] == target:
                    return True
                elif matrix[top][down_mid] > target:
                    right = down_mid - 1
                    down_mid = (right + left) // 2
                else:
                    left = down_mid + 1
                    down_mid = (right + left) // 2
            top += 1
            left, right, down_mid = 0, len(matrix[0]) - 1, (left + right)//2

        print(top, up_mid, bottom)
        return False



a = Solution()
a = a.searchMatrix([[1],[2]], 1)
print(a)