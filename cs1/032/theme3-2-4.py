def double(xs):
    c_xs = xs.copy()
    i = 0
    while i < len(c_xs):
        c_xs[i] *= 2
        i += 1
    return c_xs

# 動作確認
numbers = [1,2,3]
print(double(numbers))
print(double(numbers))