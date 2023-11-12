class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sc1, sc2 = 0, 0

        def dv(ns):
            print(ns)
            if ns is None:
                return False, ns, 0
            elif len(ns) == 1:
                print('=====')
                points = ns.pop()
                print('---')
                return False, ns, points
            elif max(ns) == ns[1]:
                points = ns.pop()
                return True, ns, points
            elif max(ns) == ns[-2]:
                points = ns[0]
                ns = ns[1:]
                return True, ns, points
            else:
                points = max(ns[0], ns[-1])
                if ns[0] > ns[-1]:
                    ns = ns[1:]
                else:
                    ns.pop()
                return True, ns, points

        temp = 0
        status = True
        while status:
            if temp % 2 == 0:
                status, nums, points = dv(nums)
                sc1 += points
            else:
                status, nums, points = dv(nums)
                sc2 += points
            temp += 1
        print('------', sc1, sc2)
        return sc1 >= sc2




a = Solution()
a = a.predictTheWinner([1000,999,999,1000,555,400])
print(a)
