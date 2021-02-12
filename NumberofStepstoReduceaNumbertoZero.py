class Solution:
    def numberOfSteps (self, num: int) -> int:
        x = bin(num)
        return len(x) + x.count('1') - 3