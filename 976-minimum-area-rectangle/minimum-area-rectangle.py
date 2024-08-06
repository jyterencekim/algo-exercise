class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        """
        brute force: nC4 
        minimum.. base + height?
        can consider only adjacent pairs within the same y
        group adjs by same ys
        adjacents

        ys = (1, 3)
        x = 1, 3, 4
        """

        ys_by_x = defaultdict(list)
        for x, y in points:
            ys_by_x[x].append(y)

        xs_by_y = defaultdict(list)
        for x, y in points:
            xs_by_y[y].append(x)

        for ys in ys_by_x.values():
            ys.sort()

        for xs in xs_by_y.values():
            xs.sort()

        min_area = math.inf

        # first decide the base exhaustively, and then look for valid heights
        for x, y in points:
            bound = bisect.bisect_left(xs_by_y[y], x)
            for j in range(bound):
                prev_x = xs_by_y[y][j]
                bound_y = bisect.bisect_left(ys_by_x[x], y)
                for k in range(bound_y):
                    prev_y = ys_by_x[x][k]
                    prev_y_index = bisect.bisect_left(ys_by_x[prev_x], prev_y)
                    if prev_y_index < len(ys_by_x[prev_x]) and ys_by_x[prev_x][prev_y_index] == prev_y:
                        w = x - prev_x
                        h = y - prev_y
                        min_area = min(min_area, w * h)
        
        return min_area if min_area != math.inf else 0