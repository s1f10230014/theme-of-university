import time

def endroll(lines):
    time.sleep(1)
    for s in lines:
        print(lines(s))
        s += 1

        
endroll(['ttt','yyyy','fffff'])
    

