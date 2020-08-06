class Solution:
    def isValid(self, s: str):
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)

            elif stack:
                if c == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False

                elif c == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False

                elif c == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False

            else:
                return False

        if not stack:
            return True

        return False

Solution().isValid("[()]")
