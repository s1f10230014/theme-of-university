def consective_wins(x):

    wins_counts = 0

    count = 0

    for one_x in x:

        if one_x:

            count += 1

            #このif節の処理は、ここで行わないと正常に動作しない。理由は、不明。
            if count > wins_counts:

                wins_counts = count


        elif one_x == False:
            count = 0

    return wins_counts





print(consective_wins([True,True,False]))

print(consective_wins([False,True,True,False,True,False,True,True,True,True,False,True]))




