def mergeArrays(a, b):
    a.append(float('inf'))
    b.append(float('inf'))
    res = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1

        else:
            res.append(b[j])
            j += 1

    return res


if __name__ == '__main__':
    a = [1,5,7,7]
    b = [0,1,2,3]
    print(mergeArrays(a, b))

# 01123577