def get_pumps(di, p):
    d = 0
    pumps = []
    for i in range(len(di)):
        x = di[i] - di[i-1] if i > 0 else di[i]
        d += x
        if d > p:
            pumps.append(di[i-1])
            d = x
    return pumps


if __name__ == '__main__':
    di = [5, 18, 25, 39, 51, 57, 66, 69, 71, 79, 86]
    p = 15
    print(get_pumps(di,p))