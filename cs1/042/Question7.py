def summer_percentage(temp):

    midsummer_day_count = 0

    for one_temp in temp:

        if one_temp >= 30:

            midsummer_day_count += 1

    midsummer_day_persent = int(midsummer_day_count / len(temp) * 100)

    return midsummer_day_persent

temp = [29,28,27,27,31,32,33,28,27,33]

print(summer_percentage(temp), '%')

