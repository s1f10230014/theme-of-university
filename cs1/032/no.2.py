def month_to_str(m):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    #括弧の種類注意
    return months[m - 1]

print(month_to_str(3))
print(month_to_str(12))

def date(m ,d):
    return month_to_str(m) + str(d)

print(date(3, 4))