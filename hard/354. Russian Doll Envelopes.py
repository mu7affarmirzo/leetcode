class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        print(sorted(envelopes))
        # w = []
        # h = []
        # for i in envelopes:
        #     w.append(i[0])
        #     h.append(i[1])
        #
        # temp = []
        # for i in range(len(w)):
        #     if temp == None:
        #         temp.append(w[i])



a = Solution()
a = a.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])
print(a)