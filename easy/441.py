class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        l, r = 0, n
        while (r - l) != 1:
            mid = (r + l) // 2
            if (1 + mid) * mid / 2 < n:
                l = mid
            else:
                r = mid
        if (1 + r) * r / 2 == n:
            return r
        else:
            return r - 1

        # index = 2
        # while True:
        #     if (index + 1)*index//2 > n:
        #         return index - 1
        #     index += 1
        #     if index > n:
        #         break
        # return n


a = Solution()
a = a.arrangeCoins(10)
print(a)