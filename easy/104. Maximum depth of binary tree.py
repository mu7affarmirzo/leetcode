from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            l_max_depth = self.maxDepth(root.left)
            r_max_depth = self.maxDepth(root.right)

            if l_max_depth > r_max_depth:
                return l_max_depth + 1
            else:
                return r_max_depth + 1




a = Solution()
print(a.maxDepth([3,9,20,None,None,15,7]))
print(a)
