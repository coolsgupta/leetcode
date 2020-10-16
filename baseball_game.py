class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        for x in ops:
            if x == '+':
                score.append(score[-1] + score[-2])
            elif x == 'D':
                score.append(2 * score[-1])
            elif x == 'C':
                score.pop()
            else:
                score.append(int(x))

        return sum(score)