#101. Symmetric Tree

from typing import Optional
from Trees.TreeNode import TreeNode

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):

            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            else:
                outside = dfs(left.left, right.right)
                inside = dfs(left.right, right.left)
                return outside and inside

        return dfs(root.left, root.right)

