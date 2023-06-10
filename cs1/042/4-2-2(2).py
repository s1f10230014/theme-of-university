#4-2-2(2)

def overlap(xs, ys):

    same_math_list = []

    for x in xs:
        for y in ys:

            if x == y:

                same_math_list.append(y)

    return same_math_list

print(overlap([1,2,3,4,5], [2,3,5,7,11]))