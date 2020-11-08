class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_occurences = {c: i for i, c in enumerate(S)}
        res = []
        first = 0
        last = 0
        for i, c in enumerate(S):
            last = max(last, last_occurences[c])
            if i == last:
                res.append(last - first + 1)
                first = i + 1

        return res


