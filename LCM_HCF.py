if __name__ == '__main__':
    a = 90
    b = 135
    ca = a
    cb = b
    while(a!=b):
        if b > a:
            b -= a

        else:
             a -= b

    print(a)
    print(ca*cb/a)