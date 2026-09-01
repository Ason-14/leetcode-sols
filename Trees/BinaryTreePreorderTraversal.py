#144. Binary Tree Preorder Traversal

from Trees.TreeNode import TreeNode
from typing import List, Optional

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preOrder(node):
            if not node:
                return None
            
            result.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        return result