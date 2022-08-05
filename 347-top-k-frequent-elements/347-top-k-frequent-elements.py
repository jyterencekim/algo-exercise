class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequencies = [(frequency, num) for num, frequency in counter.items()]
        F = len(frequencies)
        
        # top Kth elements
        def choose_top_k_and_over(items: List[Any], k: int) -> Any:
            N = len(items)
            lo, hi = 0, N - 1
            
            def partition(l: int, h: int) -> int:
                r = random.randint(l, h)
                pivot = items[r]
                # pivot is now at h
                items[r], items[h] = items[h], items[r]
                frontier = l
                for i in range(l, h):
                    if items[i] < pivot:
                        items[frontier], items[i] = items[i], items[frontier]
                        frontier += 1
                items[h], items[frontier] = items[frontier], items[h]
                
                return frontier
            
            while lo < hi:
                p = partition(lo, hi)
                if p == k:
                    return items[k:]
                elif p < k:
                    lo = p + 1
                else:
                    hi = p - 1
            return items[lo:]
        
        top_ks = choose_top_k_and_over(frequencies, F - k)
        return [num for freq, num in top_ks]
            
            
                    
            
        
        