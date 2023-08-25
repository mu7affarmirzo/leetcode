class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(mat[0])
        for i in range(n):
            res += mat[i][i]
            print(mat[i][i], '----')
            if n-(i+1) == i:
                continue
            else:
                res += mat[i][n-(i+1)]
            print(mat[i][n-(i+1)])
        return res

a = Solution()
a = a.diagonalSum([[1,2,3],[4,5,6],[7,8,9]])
print(a)
