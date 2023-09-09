type RecentCounter struct {
    queue []int
}


func Constructor() RecentCounter {
    return RecentCounter {queue: make([]int, 0)}
}


func (this *RecentCounter) Ping(t int) int {
    valid := 0
    for pt := 0; pt < len(this.queue); pt++ {
        if t - this.queue[pt] > 3000 {
            valid = pt + 1
        } else {
            break
        }
    }
    this.queue = this.queue[valid:]
    this.queue = append(this.queue, t)
    return len(this.queue)
}


/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */