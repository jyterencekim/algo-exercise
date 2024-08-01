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
        dq, next_dq = deque(), deque()
        dq.append((root, 0))
        
        while dq or next_dq:
            if not dq:
                dq = next_dq
                next_dq = deque()
            node, level = dq.popleft()
            if not node:
                continue
            if len(levels) <= level:
                levels.append([])
            levels[-1].append(node.val)
            if level % 2 == 0:
                next_dq.appendleft((node.left, level + 1))
                next_dq.appendleft((node.right, level + 1))
            else:
                next_dq.appendleft((node.right, level + 1))
                next_dq.appendleft((node.left, level + 1))

        
        return levels