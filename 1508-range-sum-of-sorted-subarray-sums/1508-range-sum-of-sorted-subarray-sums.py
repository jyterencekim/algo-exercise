class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        
        psum = []
        for num in nums:
            psum.append((psum[-1] if psum else 0) + num)
        
        ssums = []
        for i in range(n):
            for j in range(i, n):
                ssums.append(psum[j] - (psum[i - 1] if i > 0 else 0))
        
        # returns the pivot index
        def partition(l: int, r: int) -> int:
            nonlocal ssums
            pivot = (l + r) // 2
            pivot_val = ssums[pivot]
            ssums[r], ssums[pivot] = ssums[pivot], ssums[r]
            
            ptr = frontier = l
            while ptr < r:
                if ssums[ptr] < pivot_val:
                    ssums[frontier], ssums[ptr] = ssums[ptr], ssums[frontier]
                    frontier += 1
                ptr += 1
            ssums[r], ssums[frontier] = ssums[frontier], ssums[r]
            return frontier
        
        def quickselect(l: int, r: int, target: int) -> int:
            pivot = partition(l, r)
            if pivot == target:
                return pivot
            elif pivot < target:
                return quickselect(pivot + 1, r, target)
            return quickselect(l, pivot - 1, target)
                
        
        SS = len(ssums)
        r_pivot = quickselect(0, SS - 1, right - 1)
        r_sum = sum(ssums[:r_pivot + 1])
        l_pivot = quickselect(0, r_pivot, left - 1) 
        l_sum = sum(ssums[:l_pivot])
        
        return (r_sum - l_sum) % MOD