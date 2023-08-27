# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/168Q5px7BxSwfdMxBjl4r0apQmBdEhQL_
"""

import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    age = float(request.form['age'])
    sex = float(request.form['sex'])
    bmi = float(request.form['bmi'])
    bp = float(request.form['bp'])
    s1 = float(request.form['s1'])
    s2 = float(request.form['s2'])
    s3 = float(request.form['s3'])
    s4 = float(request.form['s4'])
    s5 = float(request.form['s5'])
    s6 = float(request.form['s6'])

    user_input = [[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]]
    prediction = model.predict(user_input)

    output = prediction[0]

    return render_template('index.html', prediction_text='Predicted diabetes progression: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)