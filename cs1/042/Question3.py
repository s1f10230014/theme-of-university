def consecutive_wins(x):

    count = 0
    count_list = []


    for one_x in x:

        

        if one_x == False:

            count_list.append(count)

            count = 0

        count += 1

        

    max_count = max(count_list)

    return max_count

print(consecutive_wins([True, True,False]))

print(consecutive_wins([False, True, True, False, True, False, True, True, True, True]))  # 4 を出力



