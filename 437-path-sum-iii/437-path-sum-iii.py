# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        answer = 0
        def find(node: Optional[TreeNode], prefix_sums: List[int]):
            if not node:
                return
            if not prefix_sums:
                prefix_sums.append(0)
            
            acc_sum = prefix_sums[-1] + node.val
            complement_to_find = acc_sum - targetSum
            nonlocal answer
            answer += len([s for s in prefix_sums if s == complement_to_find])
            prefix_sums.append(acc_sum)
            
            find(node.left, prefix_sums)
            find(node.right, prefix_sums)
            prefix_sums.pop()
        
        find(root, [])
        return answer
                