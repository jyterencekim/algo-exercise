# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        roots = list()
        to_delete = set(to_delete)

        q = deque([root])

        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                q.append(node.right)
                if node.right.val in to_delete:
                    node.right = None
            if node.val in to_delete:
                if node.left:
                    roots.append(node.left)
                if node.right:
                    roots.append(node.right)
        
        if root.val not in to_delete:
            roots.append(root)

        return roots

