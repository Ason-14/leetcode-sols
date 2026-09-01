#965. Univalued Binary Tree

from Trees.TreeNode import TreeNode
from typing import Optional

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        num = root.val

        def unival(node, target):
            if not node:
                return
            elif node.val == target:
                return True
            else:
                return False
            return unival(node.left, target) and unival(node.right, target)
        
        return unival(root, num)