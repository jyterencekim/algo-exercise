# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        diameter = 0
        def traverse(node: Optional[TreeNode]) -> int:
            """
            returns the path length that does traverse up to node
            """
            if not node:
                return 0
            
            l = traverse(node.left)
            r = traverse(node.right)
            nonlocal diameter
            diameter = max(diameter, l + r)
            
            return 1 + max(l, r)
        
        traverse(root)
        return diameter