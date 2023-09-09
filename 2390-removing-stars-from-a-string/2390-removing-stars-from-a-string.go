func removeStars(s string) string {
    stack := make([]rune, 0)
    STAR := '*'
    
    for _, r := range(s) {
        if r == STAR {
            stack = stack[:len(stack)-1]
            continue
        }
        stack = append(stack, r)
    }
    return string(stack)
}