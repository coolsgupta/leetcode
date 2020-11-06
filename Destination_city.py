class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src = set()
        dest = set()

        for path in paths:
            src.add(path[0])
            dest.add(path[1])

        return list(dest - src)[0]