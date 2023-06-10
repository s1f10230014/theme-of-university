def consective_wins(x):

    wins_counts = 0

    count = 0

    for one_x in x:

        if one_x:

            count += 1

        else:
            if count > wins_counts:

                wins_counts = count

                count = 0

    return wins_counts

print(consective_wins([False,True,True,False,True,False,True,True,True,True,False,True]))