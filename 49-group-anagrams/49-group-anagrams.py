class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        def normalize(s: str) -> int:
            return tuple(sorted(s))
        
        for s in strs:
            groups[normalize(s)].append(s)
        
        return groups.values()
            