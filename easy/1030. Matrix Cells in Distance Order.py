class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*cols]*rows
        print(matrix)


a = Solution()
a = a.allCellsDistOrder(1, 2, 0, 0)
print(a)