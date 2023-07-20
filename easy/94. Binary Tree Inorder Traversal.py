# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []

        def dfs(root, res):
            if root is None: return
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)
            return res

        return dfs(root, [])