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

        def search_three(upper_bound: int, target_sum: int) -> Set[Tuple[int]]:
            results = set()
            for idx in range(2, upper_bound):
                candidates = search_two(idx, target_sum - nums[idx])
                if candidates:
                    for candidate in candidates:
                        results.add(candidate + (nums[idx],))
            return results

        def search_four() -> Set[Tuple[int]]:
            results = set()
            for idx in range(3, len(nums)):
                candidates = search_three(idx, target - nums[idx])
                if candidates:
                    for candidate in candidates:
                        results.add(tuple(sorted(candidate + (nums[idx],))))
            return results
        
        return search_four()
