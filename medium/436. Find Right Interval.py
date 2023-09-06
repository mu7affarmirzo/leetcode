class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for i in range(len(intervals)):
            index = -1
            temp = None
            for j in range(len(intervals)):
                if max(intervals[i]) <= min(intervals[j]):
                    if temp == None:
                        temp = min(intervals[j])
                        index = j
                    if temp > min(intervals[j]):
                        temp = min(intervals[j])
                        index = j

            res.append(index)

        return res


a = Solution()
a = a.findRightInterval([[3,4],[2,3],[1,2]])
print(a)
x =[[1,6],[2,3],[1,2], [4,3]]
print()