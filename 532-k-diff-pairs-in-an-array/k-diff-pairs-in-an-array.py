class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        answer = 0
        for num in counts.keys():
            counts[num] -= 1
            answer += (1 if counts[num + k] > 0 else 0)
            counts[num] += 1
        
        return answer