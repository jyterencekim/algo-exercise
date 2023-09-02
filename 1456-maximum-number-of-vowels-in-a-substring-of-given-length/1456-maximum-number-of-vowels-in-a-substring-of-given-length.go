func isVowel(r byte) bool {
    VOWELS := map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true}
    return VOWELS[r]
}

func maxVowels(s string, k int) int {
    count := 0
    maxCount := 0
    
    for j, _ := range(s) {
        i := j - k + 1
        if i > 0 && isVowel(s[i - 1]) {
            count -= 1
        }
        if isVowel(s[j]) {
            count += 1
        }
        if count > maxCount {
            maxCount = count
        }
        if maxCount == k {
            return k
        }
    }
    return maxCount
}