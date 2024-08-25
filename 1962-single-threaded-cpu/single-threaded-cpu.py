class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result = list()
        work_queue = list() # heap of durations
        tasks = [(task[0], task[1], idx) for idx, task in enumerate(tasks)]
        tasks = deque(sorted(tasks, key=lambda t:t[0]))
        current_time = 0
        while tasks or work_queue:
            while tasks and tasks[0][0] <= current_time:
                task = tasks.popleft()
                heapq.heappush(work_queue, (task[1], task[2]))
            if work_queue:
                duration, index = heapq.heappop(work_queue)
                current_time += duration
                result.append(index)
                continue
            current_time = tasks[0][0]
        
        return result

