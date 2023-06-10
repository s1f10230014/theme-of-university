def change(subtotal, paid):

    change = paid - subtotal

    return change


def change_num(subtotal, paid):

    new_change = change(subtotal, paid)

    Number_of_change = 0

    for one_digit in str(new_change):

        Number_of_change += int(one_digit)

    return Number_of_change

print(change(8998, 10000))

print(change_num(8998, 10000))


    


    
