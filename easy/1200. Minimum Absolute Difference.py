class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        mini = None
        res = []
        arr = sorted(arr)
        print(arr)
        for i in range(len(arr)-1):
            res.append([arr[i], arr[i+1]])
            if mini == None:
                mini = abs(arr[i+1] - arr[i])
            elif mini > abs(arr[i+1] - arr[i]):
                print(arr[i+1], arr[i], arr[i+1] - arr[i])
                mini = abs(arr[i+1] - arr[i])
        print(mini)
        print(res)
        for i in res:
            print(i[1],i[0], i[1]-i[0])
            if (i[1]-i[0]) != mini:
                res.remove(i)
        return res


a = Solution()
a = a.minimumAbsDifference([3,8,-10,23,19,-4,-14,27])
print(a)

print([10,20,30,40][1:-1])