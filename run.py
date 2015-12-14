#! /usr/bin/python

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = 'son'
    temp_list = ['a','b','c']
    return render_template('onepage.html', name=name, temp_list=temp_list)

@app.route('/install')
def install():
	return render_template('install.html', step=5)

@app.route('/install2')
def install2():
    step = {'1': {'step':'step-1', 'Title':'Deploy Git', 'percent':30, 'desc':'aaaaaaa'},
            '2': {'step':'step-2', 'Title':'Deploy Gerrit', 'percent':50, 'desc':'bbbbbbb' },
            '3': {'step':'step-3', 'Title':'Deploy Jenkins', 'percent':100, 'desc':'ccccccc' }} 
    return render_template('install2.html', progress=step)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
