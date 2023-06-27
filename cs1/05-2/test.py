def count_char(line, c):

    count = 0

    for one_line in line:

        if one_line == c:

            count += 1

    return count

print(count_char("ざわわざわわ", "わ"))
