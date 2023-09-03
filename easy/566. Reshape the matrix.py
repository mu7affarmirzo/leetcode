class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        h = len(mat)
        l = len(mat[0])
        if h * l != r * c:
            return mat

        t = 0
        k = 0
        res = []
        for i in range(r):
            temp = []
            for j in range(c):
                print(t, k, l)
                if k == l-1:
                    temp.append(mat[t][k])
                    k = 0
                    t += 1
                else:
                    temp.append(mat[t][k])
                    k += 1

            res.append(temp)

        return res


a = Solution()
a = a.matrixReshape([[1,2, 3, 4,],[5,3,4, 6], [2,3,4,5]], 6, 2)
print(a)