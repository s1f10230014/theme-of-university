def conseal(s):
   
    new_number = ""

    for one_s in s:

        if one_s.isdigit():

            one_s = '*'

        new_number += one_s

    return new_number



    

print(conseal('090-1234-5678 is her phone number.'))

