def mod(t, n):
    rem = 0
    for i in range(len(t)):
        rem = rem*10 + int(t[i])
        rem = rem % n

    return rem

def multiple_01(base_number):
    q = []
    visited_rem = set()
    t = '1'
    q.append(t)
    while(q):
        t = q.pop(0)
        rem = mod(t, base_number)
        if rem == 0:
            return t

        if rem not in visited_rem:
            visited_rem.add(rem)
            q.append(t + '0')
            q.append(t + '1')


