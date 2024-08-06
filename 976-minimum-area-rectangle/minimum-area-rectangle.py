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

        points.sort(key=lambda p:(p[0], p[1]))
        ys_by_x = defaultdict(list)
        for x, y in points:
            ys_by_x[x].append(y)

        points.sort(key=lambda p:(p[1], p[0]))
        xs_by_y = defaultdict(list)
        for x, y in points:
            xs_by_y[y].append(x)

        min_area = math.inf

        # first decide the base exhaustively, and then look for valid heights
        for y, xs in xs_by_y.items():
            for i in range(len(xs) - 1):
                for j in range(i + 1, len(xs)):
                    xi, xj = xs[i], xs[j]
                    w = xj - xi
                    for other_y, other_xs in xs_by_y.items():
                        if other_y == y:
                            continue
                        if xi in other_xs and xj in other_xs:
                            h = abs(other_y - y)
                            min_area = min(min_area, h * w)
        
        return min_area if min_area != math.inf else 0