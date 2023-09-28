class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        x = 0
        y = 0
        for i in points:
            if i[0] > x:
                x = i[0]
            if i[1] > y:
                y = i[1]
        return x*y/2


a = Solution()
a = a.largestTriangleArea([[1,0],[0,0],[0,1]])
print(a)