def repdigit(nums):

    same_digit_list = []

    for one_num in nums:

        one_num = str(one_num)

        set_one_num = set(one_num)

        if len(set_one_num) == 1:

            same_digit_list.append(one_num)

    return same_digit_list

print(repdigit([123, 333, 88, 434, 90]))
print(repdigit([345, 67,1111111111, 0, 334]))

                

