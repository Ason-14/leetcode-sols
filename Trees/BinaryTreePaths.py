#257. Binary Tree Paths

from typing import List, Optional
from Trees.TreeNode import TreeNode

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # traverse the tree
        # initialise list
        result = []

        # helper function
        def dfs(node: Optional[TreeNode], current_path: str) -> None:
            if not node:
                return

            if current_path == "":
                current_path += f"{node.val}"
            else:
                current_path += f"->{node.val}"

            if not node.left and not node.right: # current node is a leaf
                result.append(current_path)
                return
            
            dfs(node.left, current_path)
            dfs(node.right, current_path)
        
        dfs(root, "")
        return result