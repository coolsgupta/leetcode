from collections import Counter


def pairSummingToPowerOfTwo(a):

    x = 1
    targets = {x}
    m_a = max(a) * 2
    while(x < m_a):
        x *= 2
        targets.add(x)

    counter = {}
    for i, x in enumerate(a):
        if x not in counter:
            counter[x] = []

        counter[x].append(i)

    counts = 0
    for i,  x in enumerate(a):
        for y in counter:
            if (a[i] + y) in targets:
                j = 0
                while(j < len(counter[y]) and counter[y][j] < i):
                    j += 1

                counts += len(counter[y]) - j

    return counts

if __name__ == '__main__':
    case = [1, -1, 2, 3]
    res = pairSummingToPowerOfTwo(case)
    print(res)