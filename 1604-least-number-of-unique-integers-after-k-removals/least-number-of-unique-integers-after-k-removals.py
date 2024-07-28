class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        frequencies = deque(sorted([(freq, val) for val, freq in counter.items()]))

        while k:
            f, _ = frequencies[0]
            if f > k:
                break
            k -= f
            frequencies.popleft()
        
        return len(frequencies)