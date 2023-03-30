class Solution:

    def __init__(self, nums: List[int]):
        self.original = list(nums)

    def reset(self) -> List[int]:
        return list(self.original)
        
    def shuffle(self) -> List[int]:
        orders = [i for i in range(len(self.original))]
        random.shuffle(orders)
        return [self.original[orders[i]] for i in range(len(self.original))]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()