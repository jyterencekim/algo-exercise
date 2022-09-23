class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        """
        return the max number of unique flavors of candy you can keep
        """
        kinds = set(candies)

        if k == 0:
            return len(kinds)
        if k >= len(candies):
            return 0


        counter = Counter(candies)

        # base case
        for i in range(k):
            candy = candies[i]
            counter[candy] -= 1

            if counter[candy] == 0:
                kinds.remove(candy)

        max_kept = len(kinds)


        for i in range(k, len(candies)):
            new_candy = candies[i]
            counter[new_candy] -= 1
            old_candy = candies[i - k]
            counter[old_candy] += 1

            if counter[old_candy] == 1:
                kinds.add(old_candy)
            if counter[new_candy] == 0:
                kinds.remove(new_candy)

            max_kept = max(max_kept, len(kinds))

        # ~ 21:19
        return max_kept