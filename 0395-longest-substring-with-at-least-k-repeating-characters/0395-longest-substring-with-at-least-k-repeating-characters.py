class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def satisfies(counter: Counter) -> bool:
            return all(count >= k for count in counter.values())
        
        def solve(s: str) -> int:
            counts = []
            for c in s:
                last = counts[-1] if counts else Counter()
                counts.append(last + Counter({c: 1}))

            longest = 0
            for end in range(len(s)):
                for start in range(end + 1):
                    count = counts[end] - counts[start - 1] if start > 0 else counts[end]
                    if satisfies(count):
                        length = end - start + 1
                        longest = max(longest, length)
                        break

            return longest
        
        s = list(s)
        frequencies = Counter(s)
        candidates = set()
        for c, f in frequencies.items():
            if f >= k:
                candidates.add(c)
                
        for i, c in enumerate(s):
            if c not in candidates:
                s[i] = ' '
        
        s = ''.join(s)
        targets = s.split()
        
        return max(solve(x) for x in targets) if targets else 0
        
        
                