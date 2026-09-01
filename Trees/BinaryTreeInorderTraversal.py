# 93. Binary Tree Inorder Traversal

from typing import List, Optional
from Trees.TreeNode import TreeNode

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result