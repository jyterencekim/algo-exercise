class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not n:
            return len(tasks)
        clock = 0
        left = Counter(tasks)
        requeue = dict() # index -> (task, count)
        
        while left or requeue:
            if clock in requeue:
                t, c = requeue[clock]
                left[t] = c
                del requeue[clock]
            if not left:
                clock += 1
                continue
            task, freq = left.most_common(1)[0]
            if freq > 1:
                requeue[clock + n + 1] = (task, freq - 1)
            del left[task]
            clock += 1
        
        return clock
            