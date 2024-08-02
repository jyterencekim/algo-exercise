# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0

        def dfs(node: Optional[TreeNode], prefix_sum: List[int]) -> None:
            if not node:
                return
            prefix_sum.append(prefix_sum[-1] + node.val)
            for ps in prefix_sum[:-1]:
                if targetSum == prefix_sum[-1] - ps:
                    nonlocal count
                    count += 1
            dfs(node.left, prefix_sum)
            dfs(node.right, prefix_sum)
            prefix_sum.pop()
        
        dfs(root, [0])
        return count
