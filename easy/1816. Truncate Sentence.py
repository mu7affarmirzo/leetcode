class Solution(object):
    def truncateSentence(self, txt, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        txt = txt.split()
        return "".join(txt[:k])
