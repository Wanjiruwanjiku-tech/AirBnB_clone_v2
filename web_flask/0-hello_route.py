#!/usr/bin/python3
"""
The script starts a Flask web app

The application:
    must listen on 0.0.0.0, port 5000
    routes / display 'Hello HBNB'
"""
# Import the Flask class
from flask import Flask

# Create an instance of Flask class
app = Flask(__name__)

# Bind our function to a url and use the strict_slashes=False option
@app.route('/', strict_slashes=False)
def index():
    """
    The index function.
    
    Keyword arguments:
    Takes no arguments
    Return: the text 'Hello HBNB'
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')    