class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        horizontal = [0, 0]
        horizontal_reverse = [n-1, n-1]
        vertical = [0, 0]
        vertical_reverse = [n-1, n-1]
        h_l = n
        v_l = n

        temp = 0
        m = [[]]*n

        while temp < n*n:
            m[horizontal[0]][horizontal[1]] = temp
            horizontal[1] += 1

            if n % (temp+1) == 0:
                horizontal[0] += 1

        temp += 1
