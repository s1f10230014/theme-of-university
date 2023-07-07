
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

    bc = 0

    for ty in computer:
        if you[0] == ty:

            bc += 1

        if you[1] == ty:

            bc += 1

        if you[2] == ty:


            bc += 1

        if you[3] ==ty:

            bc += 1

     
    return bc   
    

while True:

     if you == str(0000):
         
         print('終わり')
         break
        
     print('you:',you)
    
     print(hit(computer,you),'hit/',blow(computer,you),'blow')

     
     
     if computer == you:
         
         print('終わり')
         break
     
     
     
     you = input('四桁の数字を入力してください:')
     