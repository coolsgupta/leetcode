if __name__ == '__main__':
    a = 2437
    b = 875
    ca = a
    cb = b
    while(a!=b):
        if b > a:
            b -= a

        else:
             a -= b

    print(a)
    print(ca*cb/a)
