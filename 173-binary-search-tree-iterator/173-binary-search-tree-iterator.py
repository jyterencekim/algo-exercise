# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        top = self.stack.pop()
        to_return = top.val
        
        if top.right:
            node = top.right
            while node:
                self.stack.append(node)
                node = node.left
        
        return to_return

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()