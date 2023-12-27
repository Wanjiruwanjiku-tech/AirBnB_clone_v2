#!/usr/bin/python3
"""
The script starts a flask web application that listens on
port 5000 and on the host 0.0.0.0.
This particular script adds a new function
"""
# Import the flask class from flask
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Create routes for each function

@app.route('/')
def index():
    """The index function displays "Hello HBNB"
    
    Keyword arguments:
    argument -- No args
    Return: Hello HBNB
    """
    return 'Hello HBNB!'

@app.route('/hbnb')
def display_hbnb():
    """The function displays 'HBNB'
    
    Keyword arguments:
    argument -- No args
    Return: HBNB
    """
    return 'HBNB'

@app.route('/c/<text>')
def display_C_text(text):
    """The function displaya c followed by the value of the 
    text variable
    
    Keyword arguments:
    text -- The text to be displayed
    Return: C <text>
    """
    return 'C {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)