type Fn = (...params: any) => any

function memoize(fn: Fn): Fn {
    const VALUE = Symbol("VALUE");
    const delegate: Fn = fn;
    const m = new Map();
    
    return function(...args) {
        let node = m;
        for (const arg of args) {
            if (!node.has(arg)) {
                node.set(arg, new Map());   
            }
            node = node.get(arg);
        }
        if (!node.has(VALUE)) {
            node.set(VALUE, delegate(...args));
        }
        return node.get(VALUE);
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */