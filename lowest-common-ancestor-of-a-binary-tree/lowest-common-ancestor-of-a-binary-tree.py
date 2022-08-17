# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def traverse(node: TreeNode) -> Tuple[bool, bool]: # has p, has q, LCA
            if not node:
                return (False, False)
            has_p, has_q = False, False
            if node.val == p.val:
                has_p = True
            elif node.val == q.val:
                has_q = True
            
            left_has_p, left_has_q = traverse(node.left)
            right_has_p, right_has_q = traverse(node.right)
            has_p = has_p or left_has_p or right_has_p
            has_q = has_q or left_has_q or right_has_q
            if has_p and has_q:
                nonlocal ans
                if not ans:
                    ans = node
            return (has_p, has_q)
            
        traverse(root)
        return ans