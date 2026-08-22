# 100. Same Tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # both null
            return True
        elif not p or not q: # one null
            return False
        else:
            if p.val != q.val: return False
            else: pass
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)