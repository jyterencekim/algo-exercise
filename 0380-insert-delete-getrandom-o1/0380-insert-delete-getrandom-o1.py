class RandomizedSet:

    def __init__(self):
        self.idx_by_val = dict() # k = member, v = idx
        self.members = list()

    def insert(self, val: int) -> bool:
        is_new = val not in self.idx_by_val
        
        if is_new:
            self.members.append(val)
            self.idx_by_val[val] = len(self.members) - 1
        
        return is_new
        

    def remove(self, val: int) -> bool:
        existed = val in self.idx_by_val
        
        if existed:
            last_member, idx = self.members[-1], self.idx_by_val[val]
            self.members[idx] = last_member
            self.idx_by_val[last_member] = idx
            
            self.members.pop()
            del self.idx_by_val[val]
        
        return existed
        

    def getRandom(self) -> int:
        return choice(self.members)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()