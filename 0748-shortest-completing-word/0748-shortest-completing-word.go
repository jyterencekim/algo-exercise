func ToFrequency(word string) map[rune]int {
    frequency := make(map[rune]int)
    for _, c := range(word) {
        if !('a' <= c && c <= 'z') {
            continue
        }
        frequency[c] += 1
    }
    return frequency
}

// whether a encompasses b
func Encompasses(a map[rune]int, b map[rune]int) bool {
    for k, f := range(b) {
        if a[k] < f {
            return false
        }
    }
    return true
}

func shortestCompletingWord(licensePlate string, words []string) string {
    requiredFrequency := ToFrequency(strings.ToLower(licensePlate))
    
    var answer string
    
    for _, word := range(words) {
        frequency := ToFrequency(word)
        if Encompasses(frequency, requiredFrequency) && (answer == "" || len(word) < len(answer)) {
            answer = word
        }
    }
    
    return answer
}