def repdigit(nums):

    copy_nums = str(nums)

    same_list = []

    for one_num in copy_nums:

        if len(one_num) == 1:

            same_list.append(one_num)

        
    for one_num in copy_nums:

        loop_count =0

        for one_digit in one_num:

            if one_num[0] != one_digit:


                break

            same_list.append(one_num)

    return same_list





            



print(repdigit([123, 333, 88, 434, 90]))