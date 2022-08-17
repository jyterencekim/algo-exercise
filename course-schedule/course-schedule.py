class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(set)
        status = defaultdict(int)
        VISITING, VISITED = -1, 1
        
        for x, req in prerequisites:
            prereq[x].add(req)
            
        def explore(course: int) -> bool:
            nonlocal status, prereq
            if status[course] == VISITING:
                return False
            if status[course] == VISITED:
                return True
            status[course] = VISITING
            res = all(explore(req) for req in prereq[course])
            status[course] = VISITED
            return res
        
        return all(explore(course) for course in range(numCourses))
            