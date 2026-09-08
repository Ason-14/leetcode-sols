#110. Balanced Binary Tree

from typing import Optional
from Trees.TreeNode import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # dfs(...) returns boolean
        # Base case(s): not root -> True
        # Smaller problem(s): dfs(left), dfs(right)
        # Combine: left AND right
        # anomaly: height/depth > 1

        if not root:
            return True

        # helper function: track max depth
        def height(root) -> int:
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            
            return 1 + max(left, right)
        
        if abs(height(root.left) - height(root.right)) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)