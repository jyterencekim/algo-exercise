class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)] # version, value
        self.version = 0

    def set(self, index: int, val: int) -> None:
        entry = (self.version, val)
        snapshots = self.arr[index]
        candidate_index = bisect.bisect_left(snapshots, (self.version, -math.inf))
        if candidate_index == len(snapshots):
            snapshots.append(entry)
        else:
            snapshots[candidate_index] = entry

    def snap(self) -> int:
        self.version += 1
        return self.version - 1
        

    def get(self, index: int, snap_id: int) -> int:
        snapshots = self.arr[index]
        candidate_index = bisect.bisect_left(snapshots, (snap_id, math.inf)) - 1

        if candidate_index < 0:
            return 0
            
        entry = snapshots[candidate_index]
        if entry[0] > snap_id:
            return 0
        return entry[1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)