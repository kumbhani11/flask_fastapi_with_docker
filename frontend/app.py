from flask import Flask, render_template
import requests
import os


app=Flask(__name__,template_folder='templates')

@app.route('/')
def hello():
    return render_template(f'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')