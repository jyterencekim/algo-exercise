function createCounter(n: number): () => number {
    let currentCount: number = n;
    return function() {
        return currentCount++;
    }
}


/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */