class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def can_compound(x: str, y: str) -> bool:
            return all(xc not in y for xc in x)
        
        max_len = 0
        arr = [x for x in arr if len(set(x)) == len(x)]
        
        N = len(arr)
        def find(ptr=0, acc="", acc_len=0):
            if ptr == N:
                nonlocal max_len
                max_len = max(max_len, acc_len)
                return
            word = arr[ptr]
            if can_compound(acc, word):
                find(ptr + 1, acc + word, acc_len + len(word))
            find(ptr + 1, acc, acc_len)
        
        find()
        return max_len
        
        