class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # if low %2 == 1 and high %2 ==1:
        #     return (high-low)//2 + 1
        if low %2 == 0 and high % 2 ==0:
            return (high-low)//2
        else:
            return (high-low)//2 + 1

a = Solution()
a = a.countOdds(2, 11)
print(a)