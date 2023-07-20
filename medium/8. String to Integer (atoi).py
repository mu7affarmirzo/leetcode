class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = ''
        sign = ''
        for i in str(s):
            if i == " " or i.isdigit():
                if i.isdigit():
                    temp += i
            elif i == "-" or i == "+":
                sign += i
            else:
                break

        if len(temp) > 0:
            if sign == '-':
                num = int(sign+temp)
                if num < -2147483648:
                    return -2147483648
                return num
            elif len(sign) > 1:
                return 0
            else:
                if int(temp) > 2147483647:
                    return 2147483647
                return int(temp)
        else:
            return 0

s = Solution()
a = s.myAtoi('+-12')
print(a)