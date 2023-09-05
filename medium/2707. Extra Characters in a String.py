class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        temp = []
        for i in dictionary:
            if i in s:
                temp.append(i)

        temp = sorted(temp, key=len)[::-1]

        for i in temp:
            s = s.replace(i, '')

        return len(s)


a = Solution()
a = a.minExtraChar("dwmodizxvvbosxxw", ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"])
print(a)
