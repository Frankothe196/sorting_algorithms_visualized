from flask import Flask, render_template ,request
import numpy as np
import time
from threading import Timer
import asyncio

app = Flask(__name__)
data=''
@app.route("/", methods=['GET', 'POST'])
def main():
    global data
    if(request.method=="GET"):
        generate_arr(20)
        return render_template("index.html", algorithm='algorithm', func=data, count=20, type='selection')
    elif(request.method=="POST"):
        type = request.form.get('algorithm')
        count = int(request.form.get('count'))
        generate_arr(count)
        return render_template("index.html", algorithm='algorithm', func=data, type=type, count=count)

def generate_arr(len):
    global data
    randArr = np.random.randint(20,size=len)
    max=randArr.max()
    data= [randArr.tolist(), max]


if __name__ == '__main__':
    app.run(debug=True)
