class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :rtype: int
        """
        left, right = 0, len(arr) - 1
        mid = (left + right) // 2

        while left < right:
            print(left, mid, right)
            print(arr[mid - 1], arr[mid], arr[mid + 1])
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid, arr[mid]
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                left = mid
                mid = (left + right) //2
            else:
                right = mid
                mid = (left + right) // 2
        return False

a = Solution()
a = a.peakIndexInMountainArray([1,3,2,1,0])
print(a)