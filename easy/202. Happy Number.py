class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        list_of_digits = [int(x) for x in str(n)]
        temp = 0
        for i in list_of_digits:
            temp += i * i
        while temp > 3:
            temp = 0
            for i in list_of_digits:
                temp += i * i
            # print(f'List: {list_of_digits}')
            # print(temp)
            list_of_digits = [int(x) for x in str(temp)]
        # print(temp)
        print(list_of_digits)
        return list_of_digits[0] == 1


a = Solution()
s = a.isHappy(7)
print(s)