def generate(n, A=[]):
    if len(A) == 2 * n:
        if valid(A):
            print("".join(A), end=' ')

    else:
        A.append('(')
        generate(n, A)
        A.pop()
        A.append(')')
        generate(n, A)
        A.pop()

def valid(A):
    bal = 0
    for c in A:
        if c == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0: return False
    return bal == 0


generate(int(input()))

