# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # root = level 0; odd level in reversed order
        # keep a deque for each level
        # if at odd level, pop right; if at even; pop left

        levels = []
        dq = deque()
        dq.append((root, 0))
        
        while dq:
            node, level = dq.popleft()
            if not node:
                continue
            if len(levels) <= level:
                levels.append(deque())
            if level % 2 == 0:
                levels[-1].append(node.val)
            else:
                levels[-1].appendleft(node.val)
            dq.append((node.left, level + 1))
            dq.append((node.right, level + 1))

        
        return levels