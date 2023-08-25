class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        s = sum(arr)
        temp = 0
        sub = 3

        while sub <= length:
            s += sum(arr[temp:sub+temp])
            temp += 1
            if sub+temp > length:
                temp = 0
                sub += 2

        return s


a = Solution()
a = a.sumOddLengthSubarrays([10, 11, 12])
print(a)
