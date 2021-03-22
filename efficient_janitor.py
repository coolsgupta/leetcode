def getN(weight):
    weight.sort()
    i = 0
    j = len(weight) - 1
    count = 0
    while(i <= j):
        if weight[j] + weight[i] <= 3:
            count += 1
            i += 1
            j -= 1

        else:
            count += 1
            j -= 1

    return count


if __name__ == '__main__':
    arr = [1.01, 1.99, 2.5, 1.5, 1.01]
    res = getN(arr)
    print(res)