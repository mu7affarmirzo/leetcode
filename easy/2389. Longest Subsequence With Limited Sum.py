class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        # if min(queries) < min(nums):
        #     return [0]
        res = []
        print(len(nums))
        for i in range(len(queries)):
            temp = []
            for j in range(len(nums)):
                print(queries[i], nums[j])
                if sum(temp) + nums[j] <= queries[i]:
                    temp.append(nums[j])
            print('-----', temp)
            res.append(len(temp))

        return res


a = Solution()
a = a.answerQueries([624082], [972985,564269,607119,693641,787608,46517,500857,140097])
print(a)

