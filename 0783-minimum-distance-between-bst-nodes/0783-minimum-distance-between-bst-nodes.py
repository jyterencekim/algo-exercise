# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []
        
        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            nonlocal values
            traverse(node.left)
            values.append(node.val)
            traverse(node.right)
        
        traverse(root)
        diffs = [y - x for (x, y) in zip(values, values[1:])]
        return min(diffs)