# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def probe(node: Optional[TreeNode], depth: int) -> int:
            if not node:
                return depth
            
            l = probe(node.left, depth + 1)
            if not l:
                return None
            r = probe(node.right, depth + 1)
            if not r:
                return None
            
            if abs(l - r) > 1:
                return None
            
            return max(l, r)
        
        depth = probe(root, 0)
        return depth is not None
            