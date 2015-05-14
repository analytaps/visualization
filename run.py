#! /usr/bin/python

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = 'son'
    temp_list = ['a','b','c']
    return render_template('onepage.html', name=name, temp_list=temp_list)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
