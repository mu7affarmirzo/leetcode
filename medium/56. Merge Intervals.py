class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        l = len(intervals) - 1
        i = 0
        while (i < l):
            if (intervals[i][1] >= intervals[i + 1][0] and intervals[i][1] <= intervals[i + 1][1]):
                arr = [intervals[i][0], intervals[i + 1][1]]
                intervals.remove(intervals[i])
                intervals.remove(intervals[i])
                intervals.insert(i, arr)
                l -= 1
                i -= 1
            elif (intervals[i][1] >= intervals[i + 1][0] and intervals[i][1] >= intervals[i + 1][1]):
                intervals.remove(intervals[i + 1])
                l -= 1
                i -= 1
            i += 1
        return intervals


a = Solution()
a = a.merge([[1,4],[0,2],[3,5]])
print(a)

print(sorted([[1,4], [0,0]]))

d = {}
d['you'] = ['alice', 'bob', 'martin']
d['bob'] = ['rose', 'andy']
print(sorted([[1,1],[4,5],[2,1]]))