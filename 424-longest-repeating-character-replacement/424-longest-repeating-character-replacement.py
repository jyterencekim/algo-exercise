class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        S = len(s)
        max_len = 1
        
        left, right = 0, 0
        counter = Counter()
        while right < S:
            sublength = right - left + 1
            counter[s[right]] += 1
            chars = list((+counter).keys())
            if len(chars) == 1:
                max_len = max(max_len, sublength)
            else: 
                majority = max(chars, key=lambda k:counter[k])
                majority_count = counter[majority]
                minority_count = sublength - majority_count
                if minority_count <= k:
                    # all the minorities can be converted to the majority char
                    max_len = max(max_len, counter[majority] + minority_count)
                else:
                    counter[s[left]] -= 1
                    counter[s[right]] -= 1
                    left += 1
                    continue
            right += 1
        
        return max_len
                                
                    