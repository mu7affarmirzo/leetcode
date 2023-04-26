# from functools import reduce
#
#
# def solution(i, l):
#     nums = []
#     id = i
#     l = l
#
#     temp = l
#     for i in range(l):
#         for j in range(l):
#             if j < temp:
#                 nums.append(id)
#             id += 1
#         temp -= 1
#
#     result = reduce(lambda x, y: x ^ y, nums)
#     return result
#
#
# s = solution(17, 900000)
#
# print(s)

def xor_range(start, end):
    """
    Returns the XOR of all integers from start to end (inclusive).
    """

    def xor_0_to_n(n):
        """
        Returns the XOR of all integers from 0 to n (inclusive).
        """
        mod = n % 4
        if mod == 0:
            return n
        elif mod == 1:
            return 1
        elif mod == 2:
            return n + 1
        else:
            return 0

    return xor_0_to_n(end) ^ xor_0_to_n(start - 1)


def solution(start, length):
    """
    Returns the XOR checksum of the IDs of the workers checked by the bunny trainers.
    """
    result = 0
    for i in range(length):
        row_start = start + i * length
        row_end = row_start + length - i - 1
        result ^= xor_range(row_start, row_end)
    return result

s = solution(0, 3)

print(s)