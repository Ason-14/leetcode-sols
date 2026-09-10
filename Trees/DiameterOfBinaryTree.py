# 543. Diameter of Binary Tree

from typing import Optional
from Trees.TreeNode import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # base case: if not root
        if not root:
            return 0
        
        diameter = 0

        # helper function max_depth
        def max_depth(node: Optional[TreeNode]) -> int:
            nonlocal diameter

            if not node:
                return 0
            
            left = max_depth(node.left)
            right = max_depth(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)
        
        max_depth(root)

        return diameter
