def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('ゼロで割り算できません')
    else:
        print('結果は', result, 'です')
    finally:
        print('計算を完了しました')

divide(10, 0)