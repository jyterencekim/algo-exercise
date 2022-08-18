# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def explore(node: TreeNode) -> int:
            if not node:
                return 0
            left_depth = explore(node.left)
            right_depth = explore(node.right)
            max_depth = max(left_depth, right_depth) + 1
            nonlocal diameter
            diameter = max(diameter, max_depth - 1, left_depth + right_depth)
            return max_depth
        explore(root)
        return diameter
            