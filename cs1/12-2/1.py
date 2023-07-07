import math

while True:
    try:
        r = float(input('半径r='))
        print(r * r * math.pi)
    except:
        print('正しく数を入力してください')

        