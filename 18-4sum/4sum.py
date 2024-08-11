class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        brute force n choose 4 -> O(n^4)
        choose 1, and proceed to 3-sum on the rest with its target complement
        
        cf. 2-sum
        hash table.. O(n) time O(n) space
        
        3-sum
        -> choose nums[i] and look for 2-sum of target - nums[j] for j in 0..i-1
        O(n^2)
        """

        def search_two(upper_bound: int, target_sum: int) -> Set[Tuple[int]]:
            results = set()
            seen = set()

            for idx in range(upper_bound):
                num = nums[idx]
                if target_sum - num in seen:
                    results.add((target_sum - num, num))
                seen.add(num)
            
            return results

        def search_k(upper_bound: int, target_sum: int, k: int) -> Set[Tuple[int]]:
            if k == 2:
                return search_two(upper_bound, target_sum)

            results = set()
            for idx in range(k - 1, upper_bound):
                candidates = search_k(idx, target_sum - nums[idx], k - 1)
                if candidates:
                    for candidate in candidates:
                        results.add(tuple(sorted(candidate + (nums[idx],))))
            return results
        
        return search_k(len(nums), target, 4)
