def filter_odd(x):

    odd_number_lists = []

    for one_x in x:

        if one_x % 2 != 0:

            odd_number_lists.append(one_x)

    return odd_number_lists

print(filter_odd([1,2,3,4,5,6]))