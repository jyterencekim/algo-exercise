class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        reqs = defaultdict(set)
        indegree = defaultdict(int)
        free = {i for i in range(numCourses)}
        
        for a, b in prerequisites:
            reqs[b].add(a)
            indegree[a] += 1
            if a in free:
                free.remove(a)
                
        order = []
        to_take = deque(list(free))
        while to_take:
            course = to_take.popleft()
            order.append(course)
            
            for next_course in reqs[course]:
                indegree[next_course] -= 1
                if not indegree[next_course]:
                    to_take.append(next_course)
                    
        return order if len(order) == numCourses else []
            
                
        
        