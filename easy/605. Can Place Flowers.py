class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        zeroes = len(flowerbed) - sum(flowerbed)
        if flowerbed[0] == 0:
            return sum(flowerbed) + n <= len(flowerbed) // 2
        else:
            if len(flowerbed) % 2 == 1:
                return sum(flowerbed) + n <= len(flowerbed)//2 + 1
            else:
                return sum(flowerbed) + n <= len(flowerbed) // 2




a = Solution()
a = a.canPlaceFlowers([0,0,1,0,1], 1)
print(a)