def filter_odd(xs):
    f = []
    for o in xs:
        if o % 2 == 0:

             f.append(o)
    
    return f

print(filter_odd(list(range(20))))
