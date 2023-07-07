import random

birthday_year = int(input("誕生月日の西暦(YYYY)を入力してください:"))
birthday_month = int(input("生まれ月(MM)を入力してください:"))
birthday_day = int(input("誕生年の日付(DD)を入力してください:"))

if birthday_year < 2024 and birthday_month < 13 and birthday_month > 0 and birthday_day  < 32 and birthday_day > 0:
    seed = birthday_year + birthday_month + birthday_day
    random_number = random.randint(0, 100)
    if random_number < 20:
        print("大凶です。")
    elif random_number < 40:
        print("凶です。")
    elif random_number < 60:
        print("吉です。")
    elif random_number < 80:
        print("中吉です。")
    else:
        print("大吉です。")

else:
    print('エラー！正しい生年月日を入力してください！')
