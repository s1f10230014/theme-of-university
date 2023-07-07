x = int(input("1個目の商品の価格(円)を入力してください:"))
y = int(input("2個目の商品の価格(円)を入力してください:"))

subtotal = x + y

tax = int(subtotal * 0.1)

total = subtotal + tax

print("小計", subtotal)
print("消費税", tax)
print("合計", total)