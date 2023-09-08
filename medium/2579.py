class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        angles = 0
        res = 1
        for i in range(2, n + 1):
            print(res, n, angles)
            res = res + 4 + angles*4
            angles += 1
        return res


a= Solution()
a = a.coloredCells(4)
print(a)

x = '2.2.003'
print(x.split('.'))