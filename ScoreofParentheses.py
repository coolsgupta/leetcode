class Solution:
    def scoreOfParentheses(self, S: str) -> int:

        stack = [0]

        for x in S:
            if x == '(':
                stack.append(0)

            else:
                state = [stack.pop(), stack.pop()]
                stack.append(state[1] + max(state[0] * 2, 1))

        return stack[0]
