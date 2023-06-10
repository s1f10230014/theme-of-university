def concat(words):
    "空の文字列に代入可能"
    f = ''
    for s in words:
        f += s

    return f

print(concat(['apple', 'orange', 'banana']))
print(concat(['pen', 'pineapple', 'apple', 'pen']))