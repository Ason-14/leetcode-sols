#112. Path Sum

from typing import Optional
from Trees.TreeNode import TreeNode

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val

        if not root.left and not root.right and targetSum == 0:
            return True
        else:
            return (
            self.hasPathSum(root.left, targetSum) or
            self.hasPathSum(root.right, targetSum)
            )