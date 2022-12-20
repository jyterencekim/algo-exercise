class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_by_contents = defaultdict(set)
        PATTERN = r"(.*\..*)\((.*)\)"
        
        for directory in paths:
            ss = directory.split()
            path = ss[0]
            for s in ss[1:]:
                filename, contents = s.split('(')
                file_by_contents[contents].add(f"{path}/{filename}")
                
        for duplicate in file_by_contents.values():
            if len(duplicate) > 1:
                yield duplicate