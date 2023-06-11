def pyramid(n):
    x = 0
    for f in range(n):
        print(' ' * (n - f - 1) +'##' * x)
        x += 1

pyramid(10)