class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops is None:
            return n*m

        count = 1
        mat = [[0]*m for _ in range(n)]
        for i in ops:
            temp = 0
            for x in range(i[0]):
                for y in range(i[1]):
                    mat[x][y] += 1
                    if mat[x][y] > temp:
                        temp = mat[x][y]
                        count = 1
                    elif mat[x][y] == temp:
                        print(mat[x][y], x,y)
                        count += 1


        print('-----------------')
        for i in mat:
            for j in i:
                print(j, end=' ')
            print('\n')

        return count



a = Solution()
a = a.maxCount(3, 3, [[2,2],[3,3]])
print(a)
print(min([[2,2],[3,3], [2,1]]))