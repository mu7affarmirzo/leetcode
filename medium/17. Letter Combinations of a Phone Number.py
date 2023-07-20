class Solution(object):
    digits_map = {
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        '23'
        res = ['']
        for i in digits:
            temp = []
            for j in self.digits_map[i]:
                temp = temp + [r + j for r in res]
            res = temp

        return res

a = Solution().letterCombinations('23')
