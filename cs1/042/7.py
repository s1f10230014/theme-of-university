def check_scores(pts):

    s = True
    for l in pts:
        if l < 60:

            s = False
            
        
    return s

print(check_scores([90, 84, 35, 64, 98]))
print(check_scores([90, 84, 73, 64, 98]))