def stripe(w, h):

    count = 1


    for _ in range(h):

        if count % 2 != 0:

            print('#' * w)

        elif count % 2 == 0:

            print('+' * w)

        count += 1

stripe(8, 7)
