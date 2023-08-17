class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        temp = 0
        if dividend < 0 and divisor < 0:
            sign = 1
        elif dividend < 0 or divisor < 0:
            sign = -1
        else:
            sign = 1

        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1:
            if sign < 0:
                return -dividend
            else:
                return dividend
        while dividend >= divisor:
            dividend -= divisor
            temp += 1
        print(sign, temp)
        if sign < 0:
            return -temp
        else:
            return temp


a = Solution()
a = a.divide(7, -3)
print(a)