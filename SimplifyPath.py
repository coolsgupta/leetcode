class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for x in path:
            if x == '' or x == '.':
                continue

            if x == '..':
                try:
                    stack.pop()

                except:
                    pass

            else:
                stack.append(x)

        return '/' + '/'.join(stack)
