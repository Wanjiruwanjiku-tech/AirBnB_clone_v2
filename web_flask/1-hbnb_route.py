#!/usr/bin/python3
"""
The script starts a Flask web application
"""
# Import the Flask class from flask
from flask import Flask

# Create an instance of the flask class
app = Flask(__name__)

# Use the route decorator to bind our functions
@app.route('/', strict_slashes=False)
def index():
    """Index Function
    
    Keyword arguments:
    The function takes no args
    Return: the text Hello HBNB!
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display():
    """display function
    
    Keyword arguments:
    argument -- No args
    Return: the text HBNB
    """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')   