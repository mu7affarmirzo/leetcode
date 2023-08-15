class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        wordList = list(word)

        left = 0
        right = 0

        for i in range(len(word)):
            if word[i] == ch:
                right = i
                break

        while left < right:
            wordList[left], wordList[right] = wordList[right], wordList[left]
            left += 1
            right -= 1
        return "".join(wordList)


a = Solution()
s = a.reversePrefix('dabcdefd', 'z')
print(s)
