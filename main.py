from flask import Flask, render_template ,request
import numpy as np
#import time
#from threading import Timer
#import asyncio

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if(request.method=="GET"):
        data = generate_arr(20)
        return render_template("index.html", algorithm='algorithm', func=data, count=20, type='selection')
    elif(request.method=="POST"):
        type = request.form.get('algorithm')
        count = int(request.form.get('count'))
        data = generate_arr(count)
        legend=''
        if(type=='selection'):
            legend=[['complete','#fff'],['current','#000'],['complete','#fff']]
        elif(type=='bubble'):
            legend=[['complete','#fff'],['current','#000'],['complete','#fff']]
        elif(type=='merge'):
            legend=[['complete','#fff'],['current','#000'],['complete','#fff']]
        elif(type=='quick'):
            legend=[['complete','#fff'],['current','#000'],['complete','#fff']]

        return render_template("index.html", algorithm='algorithm', func=data, type=type, count=count, legend=legend)

def generate_arr(len):
    randArr = np.random.randint(20,size=len)
    max=randArr.max()
    data= [randArr.tolist(), max]
    return data


if __name__ == '__main__':
    app.run(debug=True)
