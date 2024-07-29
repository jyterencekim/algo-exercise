class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack = []

        for d in dirs:
            if d == '.' or not d:
                continue
            elif d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        
        return '/' + '/'.join(stack)