def sqrt(x):

    xn = x 
    
    for i in range(9):
        xn -= (xn**2 - x) / (2*xn)
    
    return xn

print(sqrt(2))