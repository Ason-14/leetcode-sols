#2331. Evaluate Boolean Binary Tree

from typing import Optional
from Trees.TreeNode import TreeNode

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        elif root.val == 0:
            return False
        elif root.val == 1:
            return True
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)