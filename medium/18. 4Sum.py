# class Solution(object):
#     def fourSum(self, nums_list, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         i = 0
#         j = len(nums_list) - 1
#         nums = sorted(nums_list)
#         print(nums)
#         res = []
#         while i < j:
#             q, k = i + 1, j - 1
#             outer_temp = nums[i] + nums[j]
#             temp = 0
#             inner_temp = 0
#             print('i, j', i, j)
#             print('q, k', q, k)
#             while q < k:
#                 print('----- q, k', q, k)
#                 print('========temp + nums[q] + nums[k]', outer_temp, nums[q], nums[k])
#                 inner_temp = nums[q] + nums[k]
#                 temp = outer_temp + inner_temp
#                 if temp == target:
#                     if [nums[i], nums[q], nums[k], nums[j]] not in res:
#                         res.append([nums[i], nums[q], nums[k], nums[j]])
#                     q += 1
#                     k -= 1
#                 elif temp > target:
#                     k -= 1
#                 elif temp < target:
#                     q += 1
#
#             print('Inner', temp)
#             if temp > target:
#                 print('111111')
#                 # if abs(nums[i+1]-nums[i]) > abs(nums[j]-nums[j-1]):
#                 #     j -= 1
#                 # else:
#                 #     i += 1
#                 j -= 1
#             elif temp < target:
#                 print('00000')
#                 if abs(nums[i+1]-nums[i]) > abs(nums[j]-nums[j-1]):
#                     j -= 1
#                 else:
#                     i += 1
#             else:
#                 if inner_temp == target:
#                 i += 1
#                 j -= 1
#         return res

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return

        # solve 2-sum
        if N == 2:
            l, r = 0, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):
                if target < nums[i]*N or target > nums[-1]*N:
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return


a = Solution()
s = a.fourSum([-3,-2,-1,0,0,1,2,3], 0)
print(s)





