def count_odd(nums):
    c = 0
    for s in (nums):
        if s % 2 ==0:
            c +=1
    return c

print(count_odd(list(range(20))))