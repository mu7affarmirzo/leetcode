import time

x = time.time()


def quick(nums):

    if len(nums) < 2:
        print('-------', nums)
        return nums
    else:
        pivot = nums[len(nums) // 2]
        left = [i for i in nums if pivot >= i and i != len(nums)//2]
        print(left)
        right = [i for i in nums if i > pivot]
        return quick(left) + [pivot] + quick(right)
#
#
a = quick([5,2,3,1])
print(a)

for i in range(0, -1-1, -1):
    print(i)