from collections import Counter


def arraySummation(inputs, tests):
    targets = set(tests)

    freq = Counter(inputs)

    # for i, x in enumerate(inputs):
    #     for y in inputs[i + 1:]:
    #         if (x + y) in targets:
    #             return True

    for t in targets:
        for x in freq:
            comp = (t - x)
            if comp in freq:
                if (comp != x) or (comp == x and freq[comp] > 1):
                    return True

    return False

if __name__ == '__main__':
    res = arraySummation([9, 6, 12], [1, 2, 3])
    print(res)