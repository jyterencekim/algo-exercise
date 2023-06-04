class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        N = len(pushed)
        pointer_push, pointer_pop = 0, 0
        
        while pointer_push < N and pointer_pop < N:
            stack.append(pushed[pointer_push])
            while pointer_pop < N and stack and popped[pointer_pop] == stack[-1]:
                stack.pop()
                pointer_pop += 1
            pointer_push += 1
        
        return not stack
            
            
            