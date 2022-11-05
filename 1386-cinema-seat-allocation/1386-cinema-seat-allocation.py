class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        COLS = 10
        GROUP = 4
        
        left_taken = defaultdict(bool)
        center_left_taken = defaultdict(bool)
        center_right_taken = defaultdict(bool)
        right_taken = defaultdict(bool)
        
        taken = set()
        for r, seat in reservedSeats:
            taken.add(r)
            if 8 <= seat <= 9:
                right_taken[r] = True
            elif 2 <= seat <= 3:
                left_taken[r] = True
            elif 4 <= seat <= 5:
                center_left_taken[r] = True
            elif 6 <= seat <= 7:
                center_right_taken[r] = True
        
        availables = 0
        for r in taken:
            available = max(int(not center_left_taken[r] and not center_right_taken[r]),\
                            int(not left_taken[r] and not center_left_taken[r]) + int(not center_right_taken[r] and not right_taken[r]))
            availables += available
        
        not_takens = n - len(taken)
        availables += (2 * not_takens)
        return availables