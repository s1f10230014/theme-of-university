def fact(n):

    result = 1

    #リスト、rangeに対するスライスの違いに注意 ※両方～未満
    for i in range(1,n + 1):

        result *= i

    return result

print(fact(3))

print(fact(5))