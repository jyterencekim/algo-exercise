# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer = None
        def count(node: Optional[TreeNode], target: int) -> int:
            if not node:
                return 0
            l = count(node.left, target)
            r = count(node.right, target - l - 1)
            if l + 1 == target:
                nonlocal answer
                answer = node.val
            return l + r + 1
        count(root, k)
        return answer