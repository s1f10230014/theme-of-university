#4-2-2(1)

def is_prime(x):

    count = 2

    while count < x:

        if x % count == 0:

            return False
        
        count += 1
        
    return True

print(is_prime(7))
print(is_prime(8))



         