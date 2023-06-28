from flask import Flask
from datetime import datetime

time = datetime.now()

app = Flask(__name__)

@app.route('/greeting')
def greet():

    if time.hour >= 5 and time.hour < 12:

        return 'Good Morning!'
    
    elif time.hour >= 12 and time.hour < 17:

        return 'Good Afternoon!'
    else:
        return 'Good Evening!'

app.debug = True
app.run()
