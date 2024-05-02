# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # recursive
        # 1 + right zigzag of left child or vice versa
        global_max = 0
        def zigzag(node: Optional[TreeNode]) -> Tuple[int]: 
            """
            returns (zigzag length to the left, to the right)
            """
            if not node:
                return 0, 0
            left = (1 + zigzag(node.left)[1]) if node.left else 0
            right = (1 + zigzag(node.right)[0]) if node.right else 0
            
            nonlocal global_max
            global_max = max(global_max, left, right)
            return left, right
        
        zigzag(root)
        return global_max