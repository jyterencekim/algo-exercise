# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse_preorder(root: TreeNode, is_left_first: bool, result: List[Any]) -> None:
            if not root:
                result.append(None)
                return
            result.append(root.val)
            traverse_preorder(root.left if is_left_first else root.right, is_left_first, result)
            traverse_preorder(root.right if is_left_first else root.left, is_left_first, result)
            
        left_first = []
        right_first = []
        traverse_preorder(root, True, left_first)
        traverse_preorder(root, False, right_first)
        return left_first == right_first