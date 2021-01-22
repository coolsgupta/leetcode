class Solution:
    def isValid(self, s: str) -> bool:
        end_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []
        for x in s:
            if x in end_map:
                stack.append(end_map[x])

            elif not stack or stack[-1] != x:
                break

            else:
                stack.pop()
        else:
            if not stack:
                return True

        return False


if __name__ == '__main__':
    ans = Solution().isValid('()')
    print(ans)