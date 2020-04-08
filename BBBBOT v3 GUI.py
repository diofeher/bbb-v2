from flask import Flask  
from flask import render_template
from flaskwebgui import FlaskUI
import os

app = Flask(__name__)
ui = FlaskUI(app)


@app.route("/")
def hello():  
    return render_template('index.html')

@app.route("/start", methods=['GET'])
def start(): 
    os.system('call python src/bbb1.py')

@app.route("/stop", methods=['GET'])
def stop(): 
    os.system('python my_prog1')




if __name__ == "__main__":
    ui.run()
   