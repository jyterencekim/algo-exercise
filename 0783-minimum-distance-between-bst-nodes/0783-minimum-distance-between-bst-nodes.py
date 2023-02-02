# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_diff = math.inf
        prev = None
        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            
            traverse(node.left)
            
            nonlocal prev, min_diff
            if prev:
                min_diff = min(min_diff, node.val - prev.val)
            prev = node
            
            traverse(node.right)
        
        traverse(root)
        return min_diff