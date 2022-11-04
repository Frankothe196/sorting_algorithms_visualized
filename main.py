from flask import Flask, render_template ,request
import numpy as np
#import time
#from threading import Timer
#import asyncio

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if(request.method=="GET"):
        arrLength=30
        data = generate_arr(arrLength)
        legend=[['complete','goldenrod'],['iterator','green'],['swapped','red']]
        return render_template("index.html", algorithm='algorithm', func=data, type='selection', count=arrLength, legend=legend)
    elif(request.method=="POST"):
        type = request.form.get('algorithm')
        count = int(request.form.get('count'))
        data = generate_arr(count)
        legend=''
        if(type=='selection'):
            legend=[['complete','goldenrod'],['iterator','green'],['swapped','red']]
        elif(type=='bubble'):
            legend=[['complete','goldenrod'],['iterator','green'],['spapped','red']]
        elif(type=='merge'):
            legend=[['complete','goldenrod'],['Iterator','green']]
        elif(type=='quick'):
            legend=[['complete','goldenrod'],['Pivot','yellow'],['Swap or iterator','red'],['inactive','white']]

        return render_template("index.html", algorithm='algorithm', func=data, type=type, count=count, legend=legend)

def generate_arr(len):
    randArr = np.random.randint(20,size=len)
    max=randArr.max()
    data= [randArr.tolist(), max]
    return data


if __name__ == '__main__':
    app.run(debug=True)
