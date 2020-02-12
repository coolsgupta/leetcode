def check_subsequence(sq, s):
    if len(s) < len(sq):
        return False
    for c in s:
        if c == sq[0]:
            sq = sq[1:]
        if not sq:
            return True
    else:
        return False

if __name__ == '__main__':
    print(check_subsequence(input('SubSequence'),input('String')))