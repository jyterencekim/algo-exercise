type Node struct {
    end bool
    nexts map[rune]*Node
}

type Trie struct {
    root *Node
}

func NewNode() *Node {
    return &Node {end: false, nexts: make(map[rune]*Node, 0)}
}

func Constructor() Trie {
    root := NewNode()
    return Trie {root: root}
}


func (this *Trie) Insert(word string)  {
    node := this.root
    
    for _, c := range(word) {
        if node.nexts[c] == nil {
            node.nexts[c] = NewNode()
        }
        node = node.nexts[c]
    }
    node.end = true
}


func (this *Trie) Search(word string) bool {
    node := this.root
    
    for _, c := range(word) {
        if node.nexts[c] == nil {
            return false
        }
        node = node.nexts[c]
    }
    return node.end
}


func (this *Trie) StartsWith(prefix string) bool {
    node := this.root
    
    for _, c := range(prefix) {
        if node.nexts[c] == nil {
            return false
        }
        node = node.nexts[c]
    }
    return node != nil
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */