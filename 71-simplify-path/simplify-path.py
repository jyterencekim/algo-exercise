class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack = []

        for d in dirs:
            if d == '..':
                if stack:
                    stack.pop()
                continue
            if d == '.' or not d:
                continue
            stack.append(d)
        
        return '/' + '/'.join(stack)