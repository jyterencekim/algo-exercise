class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        backtracking?
        max profit = max(max profit taking this, max profit not taking this)
        would sorting help? 
        sorting seems necessary? not sure yet
        if sorted, should I sort by startTime or endTime?
        since we are choosing whether to take a job or not,
        let's sort by startTime
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda tuple:tuple[0])
        MAX_END = max(endTime)
        N = len(jobs)

        @lru_cache(maxsize=None)
        def get_max_profit(idx: int) -> int:
            if idx >= N:
                return 0
            
            start, end, profit = jobs[idx]
            chosen = profit + get_max_profit(bisect.bisect_left(jobs, (end, end, 0)))
            not_chosen = get_max_profit(idx + 1)
            return max(chosen, not_chosen)
        
        return get_max_profit(0)
