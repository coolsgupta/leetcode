from typing import *


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for x in s:
            if not stack or stack[-1][0] != x:
                stack.append([x, 1])

            elif stack[-1][0] == x:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

        return ''.join(map(lambda x: x[0] * x[1], stack))


if __name__ == '__main__':
    case = "deeedbbcccbdaa"
    res = Solution().removeDuplicates(case, 3)
    print(res)
