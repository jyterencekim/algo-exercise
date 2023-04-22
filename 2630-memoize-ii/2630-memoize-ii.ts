type Fn = (...params: any) => any

function memoize(fn: Fn): Fn {
    const delegate: Fn = fn;
    const m = new Map();
    
    return function(...args) {
        let ptr = m;
        if (!ptr.has(args.length)) {
            ptr.set(args.length, new Map());
            if (args.length == 0) {
                ptr.set(0, delegate(...args));
            }
        }
        ptr = ptr.get(args.length);
        for (let i = 0; i < args.length; i++) {
            const arg = args[i];
            if (!ptr.has(arg)) {
                if (i == args.length - 1) {
                    ptr.set(arg, delegate(...args));
                } else {
                    ptr.set(arg, new Map());   
                }
            }
            ptr = ptr.get(arg);
        }
        return ptr;
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