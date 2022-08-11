class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        LEFT_IS_BIGGER = 1
        RIGHT_IS_BIGGER = -1
        ARE_EQUAL = 0
        def do_compare(version_a: List[int], version_b: List[int]) -> int:
            if version_a and not version_b:
                version_b = [0]
            elif version_b and not version_a:
                version_a = [0]
            elif not version_a and not version_b:
                return ARE_EQUAL
            
            a, b = version_a[0], version_b[0]
            if a == b:
                return do_compare(version_a[1:], version_b[1:])
            elif a > b:
                return LEFT_IS_BIGGER
            else:
                return RIGHT_IS_BIGGER
        
        def to_nums(version: str) -> List[int]:
            return list(map(lambda x: int(x), version.split(".")))
        
        return do_compare(to_nums(version1), to_nums(version2))