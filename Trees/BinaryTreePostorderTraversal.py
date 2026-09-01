#145. Binary Tree Postorder Traversal

from Trees.TreeNode import TreeNode
from typing import List, Optional

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def postOrder(node):
            if not node:
                return
            postOrder(node.left)
            postOrder(node.right)
            result.append(node.val)
        
        postOrder(root)
        return result