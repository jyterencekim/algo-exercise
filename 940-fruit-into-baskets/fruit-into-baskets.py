class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        two types at max
        max subarray sum such that the subarray contains at most two types
        keep a sliding window and a counter
        - keep at most two kinds (len(+counter.keys()) <= 2)
        - while len(+counter.keys()) > 2, shrink the left, up to right
        - if left == right, break
        """
        left, right = 0, 0
        N = len(fruits)
        counter = Counter()
        active = set()
        longest = 1

        for right, fruit in enumerate(fruits):
            counter[fruit] += 1
            if counter[fruit] == 1:
                active.add(fruit)
            while len(active) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    active.remove(fruits[left])
                left += 1

            longest = max(longest, right - left + 1)
        
        return longest

