# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def sym(p, q):
            # Both nodes are None
            if not p and not q:
                return True
            
            # One is None, the other is not
            if not p or not q:
                return False
            
            # Values must match
            if p.val != q.val:
                return False
            
            # Check mirrored subtrees
            return sym(p.left, q.right) and sym(p.right, q.left)
        
        return sym(root, root)

        