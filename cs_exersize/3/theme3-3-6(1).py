n = 1

subtotal = 0

commodity_price = int(input(f'{n}個目の商品価格（円）を入力してください：'))

while True:

    if commodity_price == 'q':
          
         tax = int(subtotal * 0.1)

         total = subtotal + tax

         print("小計", subtotal)
         print("消費税", tax)
         print("合計", total)
        
         break


    else:
         n += 1

         subtotal += commodity_price

         commodity_price = (input(f'{n}個目の商品価格（円）を入力してください：'))

         if commodity_price != 'q':
              commodity_price = int(commodity_price)

              

         
         

