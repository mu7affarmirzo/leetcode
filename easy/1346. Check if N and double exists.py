class Solution:
    def checkIfExist(self, arr):
        arr = sorted(arr)
        a, b = 0, len(arr) -1
        temp = 0
        print(temp, a, b)
        while a < b:
            if arr[a] * 2 == arr[b]:
                print('ggp')
                return True
            elif arr[a] * 2 > arr[b]:
                if temp == a:
                    return False
                else:
                    a = temp
                    b -= 1
            elif arr[a] *2 < arr[b]:
                temp = a
                a += 1
        return False


a = Solution()
a = a.checkIfExist([1,2,3,5,7,11,14,17])
print(a)