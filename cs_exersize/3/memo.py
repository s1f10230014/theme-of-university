import random

# ユーザーに名前を入力してもらう
name = input("あなたの名前を教えてください：")

# ユーザーに質問をし、答えを受け取る
question = input("何か質問はありますか？：")

# ユーザーの名前と答えを組み合わせて、数値を生成する
seed = name + question

# 数値を一定範囲に収める
random_number = random.randint(0, 100)

# 数値に対応する運勢を表示する
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
