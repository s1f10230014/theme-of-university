from flask import Flask
from datetime import datetime

app = Flask(__name__)

takenoko_count = 0

kinoko_count = 0


votes = []

@app.route('/history')
def history():

    all_history_row = ''


    for one_history in votes:

        all_history_row += '<by>' + one_history + '<br>'

    return all_history_row 


    
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

    time = datetime.now()

    takenoko_count += 1

    votes.append(str(time) + ' ' + 'たけのこに投票されました')
    
    return 'たけのこへの投票サイトへようこそ'

@app.route('/kinoko')
def kinoko():

    global kinoko_count 

    time = datetime.now()

    kinoko_count += 1

    votes.append(str(time) + ' ' + 'きのこに投票されました')


    return 'きのこへの投票サイトへようこそ'
app.debug = True
app.run()
