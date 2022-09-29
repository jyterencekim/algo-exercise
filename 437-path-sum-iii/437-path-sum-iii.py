# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        answer = 0
        def check(node: Optional[TreeNode], carry: int, counter: Counter) -> None:
            if not node:
                return
            
            nonlocal target, answer
            val = node.val
            acc_sum = carry + val
            complement = acc_sum - target
            answer += counter[complement]
            
            counter[acc_sum] += 1
            check(node.left, acc_sum, counter)
            check(node.right, acc_sum, counter)
            counter[acc_sum] -= 1
        
        check(root, 0, Counter({0: 1}))
        return answer