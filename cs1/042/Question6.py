def max_cont_char(line, c):

    count = 0

    temporary_count = 0

    loop_count = 0



    for one_line in line:

        loop_count += 1

        if one_line == c:

            temporary_count += 1

           
        elif one_line != c: 

            if temporary_count > count:

                count = temporary_count

                temporary_count = 0

        if loop_count == len(line):

            if temporary_count > count:

                count = temporary_count

                temporary_count = 0




                


    return count


print(max_cont_char("おのののかのかかお","の"))

print(max_cont_char("おのののかのおかか","か"))

       





