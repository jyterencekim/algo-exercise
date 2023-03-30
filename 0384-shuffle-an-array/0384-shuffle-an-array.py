class Solution:

    def __init__(self, nums: List[int]):
        self.original = list(nums)
        self.arr = nums

    def reset(self) -> List[int]:
        return list(self.original)
        
    def shuffle(self) -> List[int]:
        for i in range(len(self.arr)):
            idx_to_swap = random.randrange(i, len(self.arr))
            self.arr[i], self.arr[idx_to_swap] = self.arr[idx_to_swap], self.arr[i]
        return self.arr
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()