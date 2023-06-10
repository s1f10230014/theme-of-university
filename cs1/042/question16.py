def my_arrow(length, dir):

    if dir == 0:

        print('<' + '-' * length)
    
    elif dir == 1:

        print('-' * length + '>')

#模範回答の方がよかった、要確認

my_arrow(5, 0)
my_arrow(4, 1)