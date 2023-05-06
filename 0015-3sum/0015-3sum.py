class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        nums = []
        for num, count in counter.items():
            nums.extend([num] * min(count, 3))
        
        N = len(nums)
        index_by_num = {num: index for index, num in enumerate(nums)}
        
        ans = set()
        for i in range(N - 1):
            for j in range(i + 1, N):
                x = nums[i] + nums[j]
                if -x in index_by_num and index_by_num[-x] > j:
                    ans.add(tuple(sorted([nums[i], nums[j], nums[index_by_num[-x]]])))
        
        return ans