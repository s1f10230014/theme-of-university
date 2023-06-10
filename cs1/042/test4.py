def sevens(nums):

    seven_list = []

    copy_nums = nums

    for one_num in copy_nums:

        last_digit = list(str(one_num)).pop()

        if last_digit == '7':

            seven_list.append(one_num)

    return seven_list

print(sevens([7, 8, 9, 17, 18, 19, 777]))



