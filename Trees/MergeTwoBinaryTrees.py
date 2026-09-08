#617. Merge Two Binary Trees

from typing import Optional
from Trees.TreeNode import TreeNode

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:# left node
        if not root2:
            return root1

        # right node
        if not root1:
            return root2
        
        # both nodes
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1