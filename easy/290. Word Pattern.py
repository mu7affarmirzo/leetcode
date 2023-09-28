class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        d = {}
        temp = s.split()
        if len(pattern) != len(temp):
            return False
        for (letter, word) in zip(pattern, temp):
            if letter in d:
                if d[letter] != word:
                    return False
            elif word in d.values():
                return False
            else:
                d[letter] = word
        return True


a = Solution()
a = a.wordPattern('abba', 'dog cat cat dog')
print(a)

x = {'a': 1, 'b': 2}
print('a' in x)