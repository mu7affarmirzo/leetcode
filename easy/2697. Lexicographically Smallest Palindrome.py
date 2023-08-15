class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        index = len(s)//2
        l = s[:index]
        r = s[-index:][::-1]
        print(l)
        print(r)
        for i in range(index):
            if l[i] == r[i]:
                continue
            else:
                print(l[i])
                print(r[i])
                if l[i] < r[i]:
                    r.replace(r[i], l[i])
                else:
                    l.replace(l[i], r[i])
        print(l)
        print(r)
        return f"{l}{s[index]}{r[::-1]}"




a = Solution()
s = a.makeSmallestPalindrome('egcfe')
print(s)
# txt = "welcome to the jungle"
#
# x = txt.count(" ")
#
# print(x)
print('a'< 'b')