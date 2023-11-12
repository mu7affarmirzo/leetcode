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
                left = []
                right = []
                pivot = num[len(num) // 2]
                for i in num:
                    if i[1] < pivot[1]:
                        left.append(i)
                    elif i[1] > pivot[1]:
                        right.append(i)
                    elif i[1] == pivot[1] and i[0] < pivot[0]:
                        left.append(i)
                    elif i[1] == pivot[1] and i[0] > pivot[0]:
                        right.append(i)

                return quick_sort_h(left) + [pivot] + quick_sort_h(right)

        envelopes_h = quick_sort_h(envelopes)
        envelopes = quick_sort(envelopes)
        return envelopes, envelopes_h
        # res = [envelopes[0]]
        # for i in range(1, len(envelopes)-1):
        #     if
        # for i in range(0, len(envelopes)-1):
        #     print(envelopes[i], '============')
        #     for j in range(i+1, len(envelopes)):
        #         print(envelopes[j])
        #     print('-------------------------------\n')
        # return envelopes


a = Solution()
a, b = a.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3], [6, 5], [2, 8]])
print(a)
print(b)

# [[2, 3], [2, 8], [5, 4], [6, 4], [6, 5], [6, 7]]
# [[2, 3], [5, 4], [6, 4], [6, 5], [6, 7], [2, 8]]

# [[2, 3], [5, 4], [6, 4], [6, 5], [6, 7]]