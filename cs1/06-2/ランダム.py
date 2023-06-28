#random表示
from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello():

    for _ in range(1):
        

        t = random.choice(['キノコ', 'タケノコ'])

        s = '今日は' + t + 'をいかがでしょうか'
    return s

app.debug = True
app.run()

@app.route('/takenoko')
def takenoko():

    choice = random.choice([kinoko, takenoko]
)
    return 'たけのこへの投票サイトへようこそ'

@app.route('/kinoko')
def kinoko():
    return 'きのこへの投票サイトへようこそ'

app.debug = True
app.run()
