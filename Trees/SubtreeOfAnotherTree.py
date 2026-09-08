#572. Subtree of Another Tree

from typing import Optional
from Trees.TreeNode import TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case
        if not root:
            return False
        
        # compare actual nodes, not val
        # use same tree (helper function)
        def sameTree(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            # both None
            if not root1 and not root2:
                return True

            # one None
            if not root1 or not root2:
                return False

            # both exist
            if root1.val != root2.val:
                return False
            
            left = sameTree(root1.left, root2.left)
            right = sameTree(root1.right, root2.right)

            return left and right
        
        # same values (check if its the exact same tree)
        if root.val == subRoot.val and sameTree(root, subRoot):
            return True

        # diff values, keep recursing
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)