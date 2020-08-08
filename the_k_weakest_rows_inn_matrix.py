class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hash_rows = {}
        for i in range(len(mat)):
            hash_rows[i] = sum(mat[i])
        sorted_rows = [x[0] for x in sorted(hash_rows.items(), key=lambda x: x[1])]
        return sorted_rows[:k]
