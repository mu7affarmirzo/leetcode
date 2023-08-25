class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        gen_l = len(grid) - 2
        gen_matrix = [[0]*gen_l]*gen_l
        print(gen_matrix)
        for i in range(gen_l):
            for j in range(gen_l):
                for p in range(i, i+3):
                    for q in range(j, j+3):
                        gen_matrix[i][j] = max(gen_matrix[i][j], grid[p][q])

        return gen_matrix


a = Solution()
a = a.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
print(a)
