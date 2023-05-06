class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        N = len(nums)
        num_indice = { num: i for i, num in enumerate(nums) }
        for i, x in enumerate(nums):
            needed_sum = -x
            for j in range(i + 1, N):
                y = nums[j]
                z = needed_sum - y
                if z in num_indice and num_indice[z] > j:
                    ans.add(tuple(sorted([x, y, z])))
        return ans
            