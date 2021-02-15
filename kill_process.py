class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        pMap = {}

        for i in range(len(pid)):
            if ppid[i] not in pMap:
                pMap[ppid[i]] = []

            pMap[ppid[i]].append(pid[i])

        # res = []
        queue = [kill]
        i = 0
        while (i < len(queue)):
            kill = queue[i]
            # res.append(kill)
            queue.extend(pMap.get(kill, []))
            i += 1

        return queue
