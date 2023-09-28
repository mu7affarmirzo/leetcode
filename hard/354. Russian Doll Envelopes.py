class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def quick_sort(num):
            if len(num) < 2:
                return num
            else:
                left = []
                right = []
                pivot = num[len(num)//2]
                for i in num:
                    if i[0] < pivot[0]:
                        left.append(i)
                    elif i[0] > pivot[0]:
                        right.append(i)
                    elif i[0] == pivot[0] and i[1] < pivot[1]:
                        left.append(i)
                    elif i[0] == pivot[0] and i[1] > pivot[1]:
                        right.append(i)

                return quick_sort(left) + [pivot] + quick_sort(right)

        def quick_sort_h(num):
            if len(num) < 2:
                return num
            else:
                pivot = num[len(num)//2]
                left = [x for x in num if x[1] < pivot[1]]
                right = [x for x in num if x[1] > pivot[1]]

                return quick_sort_h(left) + [pivot] + quick_sort_h(right)
        envelopes = quick_sort(envelopes)
        envelopes_h = quick_sort_h(envelopes)

        res = []
        left = envelopes[0]
        for i in range(1, len(envelopes)):
            pass
        return envelopes, envelopes_h


a = Solution()
a, b = a.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3], [6, 5], [2, 8]])
print(a)
print(b)

