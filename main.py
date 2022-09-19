from flask import Flask, render_template ,request
import numpy as np
app = Flask(__name__)
app.run(debug=True)

@app.route("/", methods=['GET', 'POST'])
def main():
    if(request.method=="GET"):
        return render_template("index.html",count=5, algorithm='algorithm',func=bucket_sort)
    elif(request.method=="POST"):
        if(request.form.get("algorithm")):
            algorithm = request.form.get("algorithm")
        else:
            algorithm = 'empty'
        
        if(request.form.get("count")):
            count = int(request.form.get("count"))
        else:
            count = 0
        return render_template("index.html", count=count, algorithm=algorithm)


def selection_sort():
    #selection sorting here

    #time complexity
    time={}
    time.best=""
    time.average=""
    time.worst=""
    space=""

def bubble_sort():
    #bubble sorting here

    #time complexity
    time={}
    time.best=""
    time.average=""
    time.worst=""
    space=""
    
def insertion_sort():
    #insertion sorting here

    #time complexity
    time={}
    time.best=""
    time.average=""
    time.worst=""
    space=""
    
def heap_sort():
    #heap sorting here

    #time complexity
    time={}
    time.best=""
    time.average=""
    time.worst=""
    space=""
    
def quick_sort():
    #Quick sorting here

    #time complexity
    time={}
    time.best=""
    time.average=""
    time.worst=""
    space=""
    
def bucket_sort():
    #bucket sorting here

    #time complexity
    # time={}
    # time.best=""
    # time.average=""
    # time.worst=""
    # space=""
    randArr = np.random.randint(20,size=20)
    max=randArr.max()
    print(randArr)
    print(randArr.tolist())
    lst = [x for x in range(20)]
    return [randArr.tolist(), max]
    
