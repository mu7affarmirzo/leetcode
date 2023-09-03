class Solution:
    def captureForts(self, forts):
        if 1 not in forts or -1 not in forts:
            return 0

        res = 0
        flag = False
        a, b = 0, len(forts) - 1

        for i in forts:
            if not flag and i == 1:
                flag = True
                a += 1
            elif flag and i == 0:
                res += 1
            elif flag and i == -1:
                flag = False
                a += 1
        return res




a = Solution()
a = a.captureForts([1,0,0,-1,0,0,0,0,1])
print(a)