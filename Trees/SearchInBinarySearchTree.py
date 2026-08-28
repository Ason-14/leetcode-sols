#700. Search in a Binary Search Tree

from Trees.SameTree import TreeNode
from typing import Optional

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        elif val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)