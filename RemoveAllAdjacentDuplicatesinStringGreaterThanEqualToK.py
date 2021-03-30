class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        i = 0
        while (i < len(s)):
            x = s[i]
            if not stack:
                stack.append([x, 1])

            elif stack[-1][0] != x:
                if stack[-1][1] >= k:
                    stack.pop()

                if stack and stack[-1][0] == x:
                    stack[-1][1] += 1

                else:
                    stack.append([x, 1])

            elif stack[-1][0] == x:
                stack[-1][1] += 1

            i += 1

        if stack[-1][1] >= k:
            stack.pop()

        return ''.join(map(lambda x: x[0] * x[1], stack))
