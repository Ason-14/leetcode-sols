# 938. Range Sum of BST

from Trees.TreeNode import TreeNode
from typing import Optional

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

# NOTES: old solution traversed the WHOLE TREE
# this is unnecessary because it is a BST
# if node.val < low then everything to the left of it is going to be < low
# same thing if node.val > high then everything to the right is > high
# New solution accounted for these cases

        # OLD SOLUTION
        # if not root:
        #     return 0
        # elif low <= root.val <= high:
        #     return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        # else:
        #     return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

        # NEW SOLUTION (MORE OPTIMAL)
        if not root:
            return 0
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)