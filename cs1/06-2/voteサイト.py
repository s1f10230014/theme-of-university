from flask import Flask
import random
app = Flask(__name__)

takenoko_count = 0

kinoko_count = 0

@app.route('/')
def count():
    if takenoko_count > kinoko_count:
        return str(takenoko_count) + '対' + str(kinoko_count) + 'で、タケノコの勝利です。'
    elif kinoko_count > takenoko_count:

        return str(kinoko_count) + '対' + str(takenoko_count) + 'で、キノコの勝利です。'
    
    else:
        return str(takenoko_count) + '対' + str(kinoko_count) + 'で、引き分けです。'






@app.route('/takenoko')
def takenoko():

    global takenoko_count 

    takenoko_count += 1

    
    return 'たけのこへの投票サイトへようこそ' + '(' + str(takenoko_count) + ')'

@app.route('/kinoko')
def kinoko():

    global kinoko_count 

    kinoko_count += 1
    return 'きのこへの投票サイトへようこそ' + '(' + str(kinoko_count) + ')'

app.debug = True
app.run()
