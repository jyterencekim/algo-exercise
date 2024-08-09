# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        nodes = dict() # val -> TreeNode
        parents = defaultdict(set) # TreeNode -> Set[TreeNode]
        to_delete = set(to_delete)
        visited = set()

        def prepare(node: Optional[TreeNode], parent=None) -> None:
            if not node:
                return
            nodes[node.val] = node
            parents[node] = parent
            prepare(node.left, node)
            prepare(node.right, node)
        
        def bfs(node: Optional[TreeNode]) -> None:
            q = deque([node])
            while q:
                n = q.popleft()
                visited.add(n)
                for x in (n.left, n.right, parents[n]):
                    if x and x not in visited:
                        visited.add(x)
                        q.append(x)
        
        def delete(node_val: int) -> None:
            node = nodes[node_val]
            p = parents[node]
            if p:
                if p.left == node:
                    p.left = None
                else:
                    p.right = None
            if node.left:
                parents[node.left] = None
            if node.right:
                parents[node.right] = None
            del nodes[node_val]

        prepare(root)
        for node_val in to_delete:
            delete(node_val)

        roots = []
        for v, node in nodes.items():
            if node not in visited:
                roots.append(node)
                bfs(node)
        
        return roots