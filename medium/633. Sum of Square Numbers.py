class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(c//2 + 1):
            a, b = i+1, c//2
            mid = (a+b)//2

            while a <= b:
                if a*a + mid*mid == c:
                    return True
                elif a*a + mid*mid < c:
                    a = mid + 1
                    mid = (a + b) // 2
                elif a*a + mid*mid > c:
                    b = mid - 1
                    mid = (a + b) // 2
                



a = Solution()
a = a.judgeSquareSum(1)
print(a)


