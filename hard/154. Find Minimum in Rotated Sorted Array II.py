# class Solution(object):
#     def findMin(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if nums[0] < nums[-1]:
#             return nums[0]
#         left, right = 0, len(nums) - 1
#         mid = (left + right) // 2
#         res = None
#         while left <= right:
#             print(nums[mid], nums[right])
#             if nums[mid] > nums[right]:
#                 left = mid + 1
#                 mid = (left + right) // 2
#                 res = nums[right]
#             elif nums[mid] < nums[left]:
#                 right = mid
#             else:
#                 right -= 1
#         return nums[left]
#
#
# a = Solution()
# a = a.findMin([2,2,2,0,1])
# print(a)


def with_name(name):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            if name == 'M':
                print("-----")
                result = func(*args, **kwargs)
                print("-----")
                return result
            else:
                result = func(*args, **kwargs)
                return result
        return wrapper
    return my_decorator


@with_name(name='M')
def add(a, b):
    print(5)

add(3,4)