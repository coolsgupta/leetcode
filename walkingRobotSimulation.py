from typing import *


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = 0
        y = 0
        di = 0
        ans = 0
        for cmd in commands:
            if cmd == -1:
                di = (di + 1) % 4

            elif cmd == -2:
                di = (di - 1) % 4

            else:
                for ch in range(cmd):
                    nxy = (x + dx[di], y + dy[di])
                    if nxy not in obstacles:
                        x, y = nxy
                        ans = max(ans, x**2 + y**2)

        return ans
                    