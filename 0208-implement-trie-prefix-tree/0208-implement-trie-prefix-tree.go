type Trie struct {
    isWord bool
    nexts map[byte]*Trie
}


func Constructor() Trie {
    return Trie {isWord: false, nexts: make(map[byte]*Trie, 0)}
}


func (this *Trie) Insert(word string)  {
    if len(word) == 0 {
        this.isWord = true
        return
    }
    c := word[0]
    _, ok := this.nexts[c]
    if !ok {
        this.nexts[c] = &Trie {isWord: false, nexts: make(map[byte]*Trie, 0)}
    }
    this.nexts[c].Insert(word[1:])
}


func (this *Trie) Search(word string) bool {
    if len(word) == 0 {
        return this != nil && this.isWord
    }
    c := word[0]
    next, ok := this.nexts[c]
    if !ok {
        return false
    }
    return next.Search(word[1:])
}


func (this *Trie) StartsWith(prefix string) bool {
    if len(prefix) == 0 {
        return this != nil
    }
    c := prefix[0]
    next, ok := this.nexts[c]
    if !ok {
        return false
    }
    return next.StartsWith(prefix[1:])
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */