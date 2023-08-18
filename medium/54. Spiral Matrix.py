class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []

        h = len(matrix)
        l = len(matrix[0])
        v_temp = 0
        h_temp = 0
        sign = 1

        while h > v_temp-1:
            for i in range(l-1):
                print(matrix[v_temp][i], end='->')
            l -= 1
            h_temp = l

            for i in range(abs(v_temp-h)-1):
                print(matrix[i][h_temp], end='-->')

            v_temp = abs(v_temp-h)-1
            print('V_TEMP', v_temp)



a = Solution()
a = a.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
