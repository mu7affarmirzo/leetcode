class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        temp = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                length = len(height[i:j])
                print(height[i:j])
                if temp <= min(height[i], height[j]) * length:
                    temp = min(height[i], height[j]) * length
        return temp

s = Solution()
a = s.maxArea([0, 2])
print(a)