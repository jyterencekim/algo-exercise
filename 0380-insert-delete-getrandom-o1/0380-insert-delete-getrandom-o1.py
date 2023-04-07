class RandomizedSet:

    def __init__(self):
        self.members = set()
        self.order = list()

    def insert(self, val: int) -> bool:
        is_new = val not in self.members
        
        if is_new:
            self.members.add(val)
            self.order.append(val)
        
        return is_new
        

    def remove(self, val: int) -> bool:
        existed = val in self.members
        
        if existed:
            self.members.remove(val)
            self.order.remove(val)
        
        return existed
        

    def getRandom(self) -> int:
        return self.order[random.randrange(len(self.order))]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()