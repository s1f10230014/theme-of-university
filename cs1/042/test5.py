def count(s):

    count = 0

    for one_s in s:

        if one_s == '.' or one_s == '!' or one_s == '?':

            count += 1

    return count
print(count("Hello!"))
x = count("How are you? Fine, thank you. And you?")
print(x)

