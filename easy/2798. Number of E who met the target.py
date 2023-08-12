class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        temp = 0
        for i in hours:
            print(i, target)
            if i >= target:
                print('====')
                temp += 1
        return temp

a = Solution()
s = a.numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2)
print(s)