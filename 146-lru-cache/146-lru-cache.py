class Node:
    
    def __init__(self, key: int=None, value: int=None, pre: 'Node'=None, nxt: 'None'=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.nxt = nxt
        
        
        
class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = dict()
        self.mru = Node()
        self.lru = Node() # linked-list head/tail pointers
        self.mru.nxt = self.lru
        self.lru.pre = self.mru
        self.size = 0

    def remove(self, node: Node) -> None:
        pre = node.pre
        nxt = node.nxt
        pre.nxt = nxt
        nxt.pre = pre
        
    def push_head(self, node: Node) -> None:
        node.pre = self.mru
        node.nxt = self.mru.nxt
        
        self.mru.nxt.pre = node
        self.mru.nxt = node
    
    def pop_tail(self) -> Node:
        old_tail = self.lru.pre
        old_tail.pre.nxt = self.lru
        self.lru.pre = old_tail.pre
        return old_tail
        
    def refresh(self, node: Node) -> None:
        self.remove(node)
        self.push_head(node)
        
    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        curr = self.nodes[key]
        self.refresh(curr)
        return curr.value

    def put(self, key: int, value: int) -> None:
        node = self.nodes.get(key)
        
        if not node:
            new_node = Node(key, value)
            self.push_head(new_node)
            self.nodes[key] = new_node
            self.size += 1    
            
            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.nodes[tail.key]
                self.size -= 1
        else:
            node.value = value
            self.refresh(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)