class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        partitions = 1
        for c in s:
            if c in seen:
                partitions += 1
                seen = set()
            seen.add(c)
        return partitions