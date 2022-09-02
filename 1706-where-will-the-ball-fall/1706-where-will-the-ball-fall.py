class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ROWS = len(grid)
        COLS = len(grid[0])
        STUCK = -1
        states = [c for c in range(COLS)] # ith ball -> column
        
        for row in grid:
            for ball, state in enumerate(states):
                if state == STUCK:
                    continue
                direction = row[state]
                next_state = state + direction
                if not (0 <= next_state < COLS) or row[next_state] != direction:
                    states[ball] = STUCK
                    continue
                states[ball] = next_state
            
        
        return states
                