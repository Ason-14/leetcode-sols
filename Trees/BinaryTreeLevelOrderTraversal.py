#102. Binary Tree Level Order Traversal

from collections import deque
from typing import List, Optional
from Trees.TreeNode import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = deque()
        q.append(root)

        while q:
            level = []
            level_size = len(q)

            for i in range(level_size):

                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)

        return result