def anagram(s1, s2):

    s1_list = []

    s2_list = []

    for o_s1 in s1:

        s1_list.append(o_s1)

    for o_s2 in s2:

        s2_list.append(o_s2)

    #sortメソッドは、リストに対してのみ使用可能 ※sorted(), list.sort()
    s1_list.sort()

    s2_list.sort()

    count = 0

    for one_s1 in s1_list:

        if one_s1 != s2_list[count]:

            return False
        
        count += 1

    return True

print(anagram('あとうかい', 'かとうあい'))
print(anagram('domitory', 'dirtyroom'))
print(anagram('apple','orange'))
print(anagram('さとう', 'すずき'))


