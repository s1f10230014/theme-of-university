def message(name, venue, id):
    msg = """{0} さま
あなたの受験番号・受験会場は以下の通りです：
    
        ・受験番号: {2}
        ・受験会場: {1}
        
4月1日 13:00に間に合うよう、余裕をもって会場にお越しください。 """
    return msg.format(name, venue, id)

print(message('東洋 太郎', '4201教室', '00001'))