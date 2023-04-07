class RandomizedSet:

    def __init__(self):
        self.members = set()
        self.order = list()

    def insert(self, val: int) -> bool:
        is_new = val not in self.members
        self.members.add(val)
        
        if is_new:
            self.order.append(val)
        
        return is_new
        

    def remove(self, val: int) -> bool:
        existed = val in self.members
        if existed:
            self.members.remove(val)
            self.order.remove(val)
        
        return existed
        

    def getRandom(self) -> int:
        idx_to_swap = random.randrange(len(self.order))
        self.order[0], self.order[idx_to_swap] = self.order[idx_to_swap], self.order[0]
        return self.order[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()