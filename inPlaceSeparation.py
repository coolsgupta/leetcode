def inPlaceSeparation(xyInput):
    y = len(xyInput) - 1
    x = 0
    while x < y:
        if xyInput[x] == 'X':
            x += 1

        elif xyInput[y] == 'Y':
            y -= 1

        elif xyInput[y] == 'X' and xyInput[x] == 'Y':
            xyInput[x], xyInput[y] = xyInput[y], xyInput[x]
            y -= 1
            x += 1

    return xyInput

if __name__ == '__main__':
    case = ['X', 'Y', 'X', 'Y']
    print(inPlaceSeparation(case))