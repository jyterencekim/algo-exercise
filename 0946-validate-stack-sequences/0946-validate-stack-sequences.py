class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        N = len(pushed)
        pointer_pop = 0
        
        for elt in pushed:
            stack.append(elt)
            while pointer_pop < N and stack and popped[pointer_pop] == stack[-1]:
                stack.pop()
                pointer_pop += 1
        
        return not stack
            
            
            