def prepend(words, prefix):

    new_word_list = words

    new_list = []

    for one_word in new_word_list:

        new_word = prefix + one_word

        new_list.append(new_word) 

    return new_list

print(prepend(["Bean", "Sakamura", "Inoue"], "Mr. "))
words = ["rich", "power", "circle"]
result = prepend(words, "en")
print(words, result)