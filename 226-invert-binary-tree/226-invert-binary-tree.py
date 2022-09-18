# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        to_visit = [root]
        
        while to_visit:
            node = to_visit.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            to_visit.append(node.left)
            to_visit.append(node.right)
        
        return root