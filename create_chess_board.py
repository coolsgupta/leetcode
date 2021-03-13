if __name__ == '__main__':
    k = int(input())
    curr = 'W'
    res = []
    for i in range(k):
        ans = []
        for j in range(0, k):
            ans.append(curr)
            curr = 'B' if curr == 'W' else 'W'

        res.append(ans)
        curr = 'B' if curr == 'W' else 'W'

    for row in res:
        print(' '.join(row))
