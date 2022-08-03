# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

NIL = "."
DELIMITER = " "

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stack = [root]
        data = []
        
        while stack:
            node = stack.pop()
            if not node:
                data.append(NIL)
                continue
            data.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        
        return DELIMITER.join(data)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(DELIMITER)
        ptr = 0
        
        def do() -> TreeNode:
            nonlocal vals, ptr
            val = vals[ptr]
            ptr += 1
            if val == NIL:
                return None
            node = TreeNode(int(val))
            node.left = do()
            node.right = do()
            return node
            
        return do()
                
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))