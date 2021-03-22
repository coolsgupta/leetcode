def maxDifference(px):
    minP = px[0]
    maxP = float('-inf')
    res = -1
    imin = 0
    imax = -1
    for i in range(1, len(px)):
        if px[i] < minP:
            minP = px[i]
            imin = i

        elif px[i] > maxP and px[i] > minP:
            maxP = px[i]
            imax = i

        res = max(res, maxP - minP) if imax > imin else res

    return res


if __name__ == '__main__':
    case = [7,5,3,1]
    res = maxDifference(case)
    print(res)



