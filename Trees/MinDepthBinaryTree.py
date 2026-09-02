#111. Minimum Depth of Binary Tree

from Trees.TreeNode import TreeNode
from typing import Optional

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if not root.left:
            return 1 + right

        if not root.right:
            return 1 + left

        return 1 + min(left, right)