def find_pairs(a, b, target):
    c = 0
    for x in a:
        comp = target - x
        if comp in b and b[comp] > 0:
            c += a[x] * b[comp]
    return c


def task(a, b, query):
    res = []
    hashed_a = {}
    hashed_b = {}
    for x in b:
        if x not in hashed_b:
            hashed_b[x] = 0
        hashed_b[x] += 1

    for x in a:
        if x not in hashed_a:
            hashed_a[x] = 0
        hashed_a[x] += 1

    for case in query:
        if case[0] == 0:
            if case[2] not in hashed_b:
                hashed_b[case[2]] = 1
            else:
                hashed_b[case[2]] += 1
            hashed_b[b[case[1]]] -= 1

            b[case[1]] = case[2]

        else:
            res.append(find_pairs(hashed_a, hashed_b, case[1]))
    return res

res = task([1,2,3],[3,4], [[1,5],[0,0,1],[1,5]])
print(res)