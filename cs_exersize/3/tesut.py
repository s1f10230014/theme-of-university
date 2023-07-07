
you = input('四桁の数字を入力してください:')

if you == '0':

     you = str(0000)


computer = '1234'

def hit(a, b):

    hc = 0

    if computer[0] == you[0]:
        hc += 1
    
    if computer[1] == you[1]:
        hc += 1

    if computer[2] == you[2]:
        hc += 1

    if computer[3] == you[3]:
        hc += 1

    return hc

def blow (a, b):

    blow_count = 0

    for ty in computer:

        for i in range(4):

            if you[1] == ty:

                blow_count += 1
        
    return blow_count
    

while True:

     if you == str(0000):
         
         print('終わり')
         break
        
     print('you:',you)

     blow_count = blow(computer,you) - hit(computer,you)
    
     print(hit(computer,you),'hit/',blow_count,'blow')

     
     
     if computer == you:
         
         print('終わり')
         break
     
     
     
     you = input('四桁の数字を入力してください:')
     