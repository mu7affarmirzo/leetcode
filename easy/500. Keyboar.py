class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        f = set('qwertyuiop')
        s = set('asdfghjkl')
        th = set('zxcvbnm')
        temp = []

        for i in words:
            t = set(i.lower())
            if t.issubset(f):
                print(t, f)
                pass
            elif t.issubset(s):
                print(t, s)
                pass
            elif t.issubset(th):
                print(t)
                temp.append(i)
        return temp


a = Solution()
a = a.findWords(['omk'])
print(a)