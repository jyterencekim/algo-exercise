class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda tuple:tuple[0])
        N = len(jobs)

        mp = [[0 for _ in range(N)] for _ in range(2)] # 0 -> taken; 1 -> excluded

        """
        mp at idx N = max(profit by idx N + mp at idx X(after this), mp at idx N + 1)
        """

        @lru_cache(maxsize=None)
        def get_max_profit(idx: int) -> int:
            if idx >= N:
                return 0
            
            start, end, profit = jobs[idx]
            chosen = profit + get_max_profit(bisect.bisect_left(jobs, (end, end, 0)))
            not_chosen = get_max_profit(idx + 1)
            return max(chosen, not_chosen)

        def find_next_idx(end: int) -> int:
            return bisect.bisect_left(jobs, (end, end, 0))

        for idx in range(N - 1, -1, -1):
            next_idx = find_next_idx(jobs[idx][1])
            next_mp = max(mp[x][next_idx] for x in range(2)) if next_idx < N and idx + 1 < N else 0
            mp[0][idx] = jobs[idx][2] + next_mp
            mp[1][idx] = max(mp[x][idx + 1] for x in range(2)) if idx + 1 < N else 0

        
        return max(mp[x][0] for x in range(2))
