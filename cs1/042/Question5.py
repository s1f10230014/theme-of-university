def count_digit(line):

    count = 0

    for one_line in line:

        if one_line.isdigit():

            count += 1

    return count

print(count_digit("今日は5月10日"))

        