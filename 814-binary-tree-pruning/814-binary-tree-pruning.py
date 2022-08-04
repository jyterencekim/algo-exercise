# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def has_one(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            has_one_left = has_one(node.left)
            has_one_right = has_one(node.right)
            
            if not has_one_left:
                node.left = None
            if not has_one_right:
                node.right = None
            
            return node.val == 1 or has_one_left or has_one_right
        root_has_one = has_one(root)
        return root if root_has_one else None