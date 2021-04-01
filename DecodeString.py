from typing import *


# class Solution:
#     def decodeString(self, s: str) -> str:
#         i = 0
#         count = 1
#         res = ''
#         if s[i].isdigit():
#             count = 0
#             while (s[i].isdigit()):
#                 count = count*10 + int(s[i])
#                 i += 1
#
#         while(s[i].isalpha()):
#             res += s[i]
#             i += 1
#
#         if s[i] == '[':
#             res += self.decodeString(s[i+1:])
#
#         if s[i] == ']':
#             return count*res
#
#         return count * res
#
#
#


class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        charStack = []
        num = 0
        currStr = ''
        for x in s:
            if x.isdigit():
                num = num * 10 + int(x)

            elif x == '[':
                numStack.append(num)
                charStack.append(currStr)
                currStr = ''
                num = 0

            elif x == ']':
                currStr = charStack.pop() + currStr*numStack.pop()

            else:
                currStr += x

        return currStr


if __name__ == '__main__':
    case = "3[a]2[bc]"
    res = Solution().decodeString(case)
    print(res)
