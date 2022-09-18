# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def do_invert(node: Optional[TreeNode]):
            if not node:
                return
            node.left, node.right = node.right, node.left
            do_invert(node.left)
            do_invert(node.right)
        
        do_invert(root)
        return root