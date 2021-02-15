`


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                curr_clr = 0
                color[node] = curr_clr
                queue = [node]
                while (queue):
                    curr = queue.pop(0)
                    curr_clr = 1 if color[curr] == 0 else 0
                    for x in graph[curr]:
                        if x not in color:
                            color[x] = curr_clr
                            queue.append(x)

                        elif color[x] != curr_clr:
                            return False

        return True