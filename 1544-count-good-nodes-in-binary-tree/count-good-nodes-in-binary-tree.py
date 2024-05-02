# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def traverse(node: TreeNode, max_so_far=-math.inf) -> None:
            if not node:
                return
            if node.val >= max_so_far:
                nonlocal count
                count += 1
                max_so_far = node.val
            traverse(node.left, max_so_far)
            traverse(node.right, max_so_far)
        
        traverse(root)
        return count
