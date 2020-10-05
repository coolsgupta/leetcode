case = [[3,5],[1,4],[2,4],[1,5],[2,3]]

dt = {}
set_visited = set()
for pair in case:
    pair =tuple(pair)
    if pair[0] not in dt:
        dt[pair[0]] = []

    if pair[1] not in dt:
        dt[pair[1]] = []

    dt[pair[0]].append(pair)
    dt[pair[1]].append(pair)

x = case[0][0]
output = [x]
while len(set_visited) != len(case):
    for pos in dt[x]:
        if pos not in set_visited:
            y = 0 if pos[1]==x else 1
            next_x = pos[y]
            output.append(next_x)
            set_visited.add(pos)
            x = next_x
            break

print(output)