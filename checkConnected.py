def isConnected(n_nodes, edges):
    vMap = {x:set() for x in range(n_nodes)}
    for x in edges:
        vMap[x[0]].add(x[1])
        vMap[x[1]].add(x[0])

    queue = [0]
    visited = set()
    while queue:
        curr = queue.pop(0)
        visited.add(curr)
        for x in vMap[curr]:
            if x not in visited:
                queue.append(x)

    return True if len(visited) == n_nodes else False


if __name__ == '__main__':
    case = [[0,1], [2,3]]
    print(isConnected(4, case))