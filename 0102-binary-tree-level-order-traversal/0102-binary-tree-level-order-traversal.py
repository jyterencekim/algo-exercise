# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # of (node, level)
        q = deque() 
        q.append((root, 1)) 
        
        # [level - 1] -> nodes at the level
        traversed = [] 
        
        while q:
            node, level = q.popleft()
            if not node:
                continue
            if len(traversed) < level:
                traversed.append([])
            traversed[-1].append(node.val)
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
        
        return traversed
        