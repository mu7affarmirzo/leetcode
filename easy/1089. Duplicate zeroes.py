class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        if 0 not in arr:
            return arr

        temp = [0]*len(arr)
        index = 0
        i = 0
        while i < len(temp) :
            if arr[index] == 0:
                temp[i] = 0
                if i != len(arr) - 2:
                    temp[i] = 0
                i += 2
                index += 1
            else:
                temp[i] = arr[index]
                i += 1
                index += 1
        return temp


a = Solution()
a = a.duplicateZeros([1,0,2,3,0,4,5,0])
print(a)