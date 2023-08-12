# class Solution(object):
#     def generate(self, N):
#         """
#         :type rowIndex: int
#         :rtype: List[List[int]]
#         """
#         prev = 1
#         result = [1]
#         for i in range(1, N + 1):
#             # nCr = (nCr-1 * (n - r + 1))/r
#             curr = (prev * (N - i + 1)) // i
#             result.append(curr)
#             prev = curr
#         return result

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            internal = []
            for j in range(i+1):
                temp = []
                if i >= 2:
                    temp.append(0)
                    temp += result[i-1]
                    temp.append(0)
                    internal.append(temp[j] + temp[j+1])
                else:
                    internal.append(1)
            result.append(internal)
        return result


a = Solution()
s = a.generate(6)
print(s)
# # print(s[5])
# #
# # for i in s:
# #     print(i)


# def binomial_coefficients_recursive(N, i=0, prev=1, result=None):
#     if result is None:
#         result = [1]
#
#     if i == N:
#         return result
#     else:
#         curr = (prev * (N - i)) // (i + 1)
#         result.append(curr)
#         return binomial_coefficients_recursive(N, i + 1, curr, result)
#
# N = 6  # Replace this with your desired N value
# coefficients = binomial_coefficients_recursive(N)
# print(coefficients)
