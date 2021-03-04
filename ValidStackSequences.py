class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for x in pushed:
            if x == popped[0]:
                popped.pop(0)
                while (stack and stack[-1] == popped[0]):
                    popped.pop(0)
                    stack.pop()
print('yes', end=)
            else:
                stack.append(x)

        if len(popped) == 0:
            return True
        return False