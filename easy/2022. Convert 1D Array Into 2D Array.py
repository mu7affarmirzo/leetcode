class Solution(object):

    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        print(m*n)
        print(len(original))
        if m*n != len(original):
            return []
        temp = 0
        res = []
        for i in range(m):
            res.append([original[x] for x in range(temp, temp+n)])
            temp += n
        return res
        print(res)

a = Solution()
a = a.construct2DArray([3], 1,2)

