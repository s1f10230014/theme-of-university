def make_pali(s,flag):
        

    

        new_s = s

        #リストに変換する必要あり、もともとリストの場合は、list.reverse()と記述する
        reverse_new_s_list = list(reversed(new_s))

        #joinは、配列を文字列に変換することができる
        reverse_s = "".join(reverse_new_s_list)

       

        if flag == 1:
                
                #popは、リストに対してのみ有効 添え字
                reverse_new_s_list.pop(0)

                reverse_s = "".join(reverse_new_s_list)


                palindrome = s + reverse_s

        elif flag == 0:
                
                palindrome = s + reverse_s

        return palindrome

print(make_pali("ねんまつ", 0))
print(make_pali("いたりあでくらし", 1))
