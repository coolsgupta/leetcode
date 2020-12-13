def bestTrio(friends_nodes, friends_from, friends_to):
    # Write your code here
    adjacency_list = {}
    for x in range(len(friends_from)):
        adjacency_list[friends_from[x]] = adjacency_list.get(friends_from[x], []) + [friends_to[x]]
        adjacency_list[friends_to[x]] = adjacency_list.get(friends_to[x], []) + [friends_from[x]]

    trio_scores = []
    for x in adjacency_list:
        for y in adjacency_list[x]:
            for z in adjacency_list[y]:
                if z in adjacency_list[x]:
                    trio_scores.append(len(adjacency_list[x]) + len(adjacency_list[y]) + len(adjacency_list[z]) - 6)

    if not trio_scores:
        return -1

    return min(trio_scores)
