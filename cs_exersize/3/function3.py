def hit(a1,a2,a3,a4,b1,b2,b3,b4):

    h = 0

    if a1 == b1:
        h += 1
    
    if a2 == b2:
        h += 1

    if a3 == b3:
        h += 1

    if a4 == b4:
        h += 1
    h = str(h)

    return h

print ("(1234,4321) =>",hit(1,2,3,4,4,3,2,1),"hit")
print("(1234,1432) =>" , hit(1,2,3,4,1,4,3,2),"hit")