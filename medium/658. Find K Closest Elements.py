class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        a, b = 0, len(arr) - 1
        mid = (a + b) // 2
        index = None
        while a <= b:
            print(a, mid, b)
            if arr[mid] == x:
                index = mid
                break
            elif arr[mid] < x:
                a = mid + 1
                mid = (a + b) // 2
            else:
                b = mid - 1
                mid = (a + b) // 2
        if mid == len(arr) - 1 and index == None:
            index = len(arr)
        elif index == None:
            index = -1

        if index == -1:
            return arr[:k]
        elif index == len(arr):
            return arr[-4::]
        print(index)
        return arr


a = Solution()
a = a.findClosestElements([1,2,3,4,5], 4, -1)
print(a)
#
