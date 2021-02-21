class Solution:
    def romanToInt(self, s: str) -> int:
        int_map = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        last_val = int_map[s[-1]]
        total = last_val
        for x in s[::-1][1:]:
            curr = int_map[x]
            if curr < last_val:
                total -= curr
            else:
                total += curr
            last_val = curr

        return total