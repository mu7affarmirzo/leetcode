from collections import deque


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        # A queue to keep track of nodes and their level in the form (node, depth)
        queue = deque([(root, 1)])

        while queue:
            # Get the next node to visit and its depth from the front of the queue
            node, depth = queue.popleft()

            # Check if this is a leaf node
            if node.left is None and node.right is None:
                return depth

            # If this node has a left child, add the left child and the new depth to the queue
            if node.left is not None:
                queue.append((node.left, depth + 1))

            # If this node has a right child, add the right child and the new depth to the queue
            if node.right is not None:
                queue.append((node.right, depth + 1))


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

