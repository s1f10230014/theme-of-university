birthday = int(input("生年月日(yyymmdd)8桁を入力してください:"))
if birthday % 4 == 0:
    print("大吉!")
elif birthday % 4 == 1:
    print("中吉")
elif birthday % 4 == 2:
    print("小吉")
elif birthday % 4 == 3:
    print("凶")