# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -math.inf
        def get_max(node: TreeNode) -> Tuple:
            if not node:
                return 0
            left = get_max(node.left)
            right = get_max(node.right)
            
            val = node.val
            left_this = left + val
            this_right = right + val
            left_this_right = left + val + right
            
            nonlocal max_sum
            max_sum = max(max_sum, left_this, this_right, left_this_right, val)
            
            return max(left_this, this_right, val)
        
        get_max(root)
        return max_sum