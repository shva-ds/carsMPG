# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 19:48:55 2021

@author: Sheela Vatsala
"""


from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('car.pkl', 'rb'))
model = pickle.load(open("C:\\Users\\Sheela Vatsala\\car.pkl", 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['HP']
    data2 = request.form['SP']
    data3 = request.form['VOL']
    #data4 = request.form['d']
    arr = np.array([[data1, data2, data3]])
    MPG = model.predict(arr)
    return render_template('result.html', data=MPG)


if __name__ == "__main__":
    app.run(debug=True)















