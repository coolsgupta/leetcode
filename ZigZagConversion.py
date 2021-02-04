class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        strings = [""] * numRows
        dx = -1
        di = 0
        s = list(s)
        for i in range(len(s)):
            strings[di] = strings[di] + s[i]
            if di == 0 or di == numRows - 1:
                dx = -dx
            di += dx

        return ''.join(strings)
