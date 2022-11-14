from flask import Flask, render_template ,request
import numpy as np

app = Flask(__name__)

# There will only be one available route for this app as it is a single page app with a simple APIs
@app.route("/", methods=['GET', 'POST'])
def main():
    # Display the defauly starting screen
    if(request.method=="GET"):
        arrLength=30
        data = generate_arr(arrLength)
        legend=[['complete','goldenrod'],['iterator','green'],['swapped','red']]
        return render_template("index.html", algorithm='algorithm', func=data, type='selection', count=arrLength, legend=legend)
    # When a user interacts with the input form
    elif(request.method=="POST"):
        type = request.form.get('algorithm')
        count = int(request.form.get('count'))
        data = generate_arr(count)
        legend=''
        # Setting the legenf for the selected algorithm
        if(type=='selection'):
            legend=[['complete','goldenrod'],['iterator','green'],['swapped','red']]
        elif(type=='bubble'):
            legend=[['complete','goldenrod'],['iterator','green'],['spapped','red']]
        elif(type=='merge'):
            legend=[['complete','goldenrod'],['Iterator','green']]
        elif(type=='quick'):
            legend=[['complete','goldenrod'],['Pivot','yellow'],['Swap or iterator','red'],['inactive','white']]

        # Data shared in the response is the 1. A random array generated for sorting. 2. The number of items in the array. 2. The type of algorithm to run.  3. The legend for the selected algorithm.
        return render_template("index.html",  func=data, count=count, type=type, legend=legend)

# Generate a random array, length or array is specified in function parameter
def generate_arr(len):
    randArr = np.random.randint(30,size=len)
    max=randArr.max()
    data= [randArr.tolist(), max]
    return data


if __name__ == '__main__':
    app.run(debug=True)
