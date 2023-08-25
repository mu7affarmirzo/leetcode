class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        # arr = [f, x,x,x]
        # enc = [a, b, c]
        arr = [first, ]
        for i in range(len(encoded)):

            temp = encoded[i] ^ arr[i]
            arr.append(temp)
        return arr

a = Solution()
a = a.decode([1,2,3], 1)
print(a)
print(1^2)
print(3^1)
print(3^2)