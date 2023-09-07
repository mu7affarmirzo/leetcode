class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(queries)):
            temp = []
            max_l = 0
            a, b = 0, len(nums) - 1
            while a <= b:
                print(temp, nums[a], queries[i])
                if sum(temp) + nums[a] <= queries[i]:
                    temp.append(nums[a])
                elif sum(temp) + nums[a] > queries[i]:
                    if len(temp) > max_l:
                        max_l = len(temp)
                    temp = []
                a += 1
            res.append(max_l)
        return res



a = Solution()
a = a.answerQueries([4,5,2,1], [3,10,21])
print(a)