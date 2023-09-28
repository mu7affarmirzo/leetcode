class Solution:
    def smallestNumber(self, num):
        temp = sorted([int(x) for x in str(abs(num))])
        print(temp)
        if num < 0:
            res = ''.join([str(x) for x in temp])[::-1]
            return -int(res)

        if len(temp) > 1 and temp[0] == 0:
            i = 0
            while True:
                if temp[i] > 0:
                    temp[0], temp[i] = temp[i], temp[0]
                    break
                else:
                    i += 1

            return int(''.join([str(x) for x in temp]))
        else:
            return int(''.join([str(x) for x in temp]))


a = Solution()
a = a.smallestNumber(95005)
print(a)