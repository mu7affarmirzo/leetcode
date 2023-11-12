class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        p_l = len(part)
        l, r = 0, p_l
        while r <= len(s):
            print(s[l:r])
            if s[l:r] == part:
                print('------------', s)
                s = s[:l] + s[r:]
                print(s,'****')
                l, r = 0, p_l
            else:
                l += 1
                r += 1
        return s



a = Solution()
a = a.removeOccurrences('axxxxyyyyb', 'xy')
print(a)
