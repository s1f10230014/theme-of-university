def find(list, x):
    for one_list in list:
        
        if one_list == x:

            return True
        
    return False

print(find([1,2,3,4,5], 4))
