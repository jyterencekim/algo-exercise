func eraseOverlapIntervals(intervals [][]int) int {
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][1] < intervals[j][1]
    })

    var maxEnd int
    count := 0

    for i, interval := range(intervals) {
        if i == 0 || maxEnd <= interval[0] {
            count += 1
            maxEnd = interval[1]
        }
    }

    return len(intervals) - count
}