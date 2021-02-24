def reduceTheNumber(number, k):
    if len(number) <= k:
        return number

    n = list(map(int, number))

    res = ''
    i = 0
    while(i < len(number)):
        res = res + str(sum(n[i:i + k]))
        i += k

    if len(res) > k:
        res = reduceTheNumber(res, k)

    return res

if __name__ == '__main__':
    case = '1111122222'
    k = 3
    print(reduceTheNumber(case, k))

