def checkDiv(s, t):
    if len(s) % len(t):
        return False

    i = 0
    k = len(t)
    while i < len(s):
        if s[i: i + k] != t:
            return False
        i += k

    return (i // k)


def findSmallestDivisor(s, t):
    stage1 = checkDiv(s, t)
    if stage1:
        div = ''
        for x in t:
            div += x
            if checkDiv(t, div):
                return len(div)

    return -1


if __name__ == '__main__':
    case = ['lrbblrbb', 'lrbb']
    case = ['rbrb', 'rbrb']
    print(findSmallestDivisor(case[0], case[1]))
