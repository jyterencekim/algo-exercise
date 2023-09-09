func largestAltitude(gain []int) int {
    sum := 0
    largest := 0
    for _, g := range(gain) {
        sum += g
        if sum > largest {
            largest = sum
        }
    }
    return largest
}