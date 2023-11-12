# class Solution(object):
#     def evalRPN(self, tokens):
#         """
#         :type tokens: List[str]
#         :rtype: int
#         """
#         stack = []
#         operators = ['+', '-', '*', '/']
#         for i in tokens:
#             print(i, stack)
#             if i in operators:
#                 temp = 0
#                 if i == '+':
#                     temp = [stack[-2] + stack[-1]]
#                 elif i == '-':
#                     temp = [stack[-2] - stack[-1]]
#                 elif i == '*':
#                     temp = [stack[-2] * stack[-1]]
#                 else:
#                     print('***********************', int(stack[-2] / stack[-1]))
#                     temp = [int(stack[-2] / stack[-1])]
#                 stack.pop()
#                 stack.pop()
#                 print('----', stack)
#                 stack = stack + list(temp)
#                 print('----', stack)
#             else:
#                 stack.append(int(i))
#             print('----', stack)
#         return stack.pop()
#
#
# a = Solution()
# a = a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
# print(a)


x = '/home/../foo/'
print(x.split('/'))