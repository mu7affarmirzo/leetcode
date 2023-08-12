class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        temp = duration
        if len(timeSeries) == 1:
            return duration
        for i in range(1, len(timeSeries)):
            print(timeSeries[i], timeSeries[i-1])
            if timeSeries[i-1] + duration < timeSeries[i]:
                temp += duration
            else:
                temp += timeSeries[i] - timeSeries[i-1]

        return temp


a = Solution()
s = a.findPoisonedDuration([1,4], 2)
print(s)
