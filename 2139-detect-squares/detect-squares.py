class DetectSquares:

    def __init__(self):
        self.points_by_x = defaultdict(set)
        self.points_by_y = defaultdict(set)
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point = tuple(point)
        self.points[point] += 1
        self.points_by_x[x].add(point)
        self.points_by_y[y].add(point)
        

    def count(self, point: List[int]) -> int:
        """
        Case
        1 2
        3 4
        """
        total_count = 0
        x, y = point
        
        for bx, by in self.points_by_x[x]:
            height = y - by # candidate length
            if height == 0:
                continue
            left_x = x - height
            right_x = x + height
            left = left_x, y
            right = right_x, y
            left_diagonal = left_x, by
            right_diagonal = right_x, by
            total_count += (self.points[(bx, by)] * self.points[left] * self.points[left_diagonal]) + (self.points[(bx, by)] * self.points[right] * self.points[right_diagonal])

        return total_count


        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)