from typing import *

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        availableKeys = rooms[0]
        allKeys = {0}
        allKeys.update(availableKeys)
        visitedRooms = set()
        visitedRooms.update(availableKeys)
        while(availableKeys):
            currKeys = set()
            for x in availableKeys:
                currKeys.update(rooms[x])

            allKeys.update(currKeys)
            availableKeys = currKeys.difference(visitedRooms)
            visitedRooms.update(currKeys)
            if len(allKeys) == len(rooms):
                return True

        return True if len(allKeys) == len(rooms) else False

if __name__ == '__main__':
    case = [[1],[2],[3],[]]
    res = Solution().canVisitAllRooms(case)
    print(res)