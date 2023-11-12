class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        temp = path.split('/')
        print(temp)
        stack = []
        for i in temp:
            print(i)
            if i == '..' or i == '.':
                print('.........', stack)
                if len(stack) >= 2:
                    stack.pop()
                    stack.pop()

            elif i == '':
                print(stack)
                continue
            else:
                stack.append('/')
                stack.append(i)
        if len(stack) == 0:
            return '/'
        return ''.join(stack)


a = Solution()
a = a.simplifyPath("/a/./b/../../c/")
print(a)