# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

NIL = "."
DELIMITER = " "
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        values = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node is None:
                values.append(NIL)
                continue
            
            values.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
            
        return DELIMITER.join(values)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        values = deque(data.split(DELIMITER))
        
        def do_deserialize():
            nonlocal values
            val = values.popleft()
            
            if val == NIL:
                return None
            
            node = TreeNode(val)
            node.left = do_deserialize()
            node.right = do_deserialize()
            
            return node
        
        root = do_deserialize()
        return root
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans