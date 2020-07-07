def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    flag = True
    i = len(digits) - 1

    while (flag):
        if i == -1:
            return [1] + digits

        elif digits[i] == 9:
            digits[i] = 0

        else:
            digits[i] += 1
            flag = False

        i -= 1
    return digits


def plusOne_2(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    num = int(''.join(list(map(str, digits)))) + 1
    return list(map(int, str(num)))


if __name__ == '__main__':
    plusOne([9])
