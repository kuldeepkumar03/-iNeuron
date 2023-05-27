import pickle
import numpy as np
from flask import Flask, render_template,request, url_for,redirect

app=Flask(__name__)
model=pickle.load(open("model.pkl",'rb'))
@app.route("/")
def home():
    return render_template("new.html")

@app.route("/predict",methods=["POST"])
def predict():
    features=[int(x) for x in request.form.values()]
    final=[np.array(features)]
    prediction=model.predict(final)
    output = round(prediction[0], 1)
    
    return render_template('new.html',predict='Restaurant Rating is : {}'.format(output))

if __name__=='__main__':
    app.run(debug=True)