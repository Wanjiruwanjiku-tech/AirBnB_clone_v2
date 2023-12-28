#!/usr/bin/python3
"""
The script starts a Flask web application.
Routes:
    /                       - Displays Hello HBNB!
    /hbnb                   - displays HBNB
    /c/<text>               - displays C followed by the value in text var
    /python/(<text>)        - Python followed by the value in text var
    /number/<n> - displays number
    /number_template/<n>    - displays a html page only if n is an integer

The strict_slashes=False option must be used in the definition.
"""
# Import the required classes and functions
from flask import Flask, abort
from flask import render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Create the required routes and their functions
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    The function displays "Hello HBNB!"
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    displays HBNB
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def method_name(text):
    """
    Displays the text C followed by the value
    of the variable text

        text - the value to display
    """
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    """The Function displays Python followed by
    the value of the text variable
    
    Keyword arguments:
    text -- Contains the value to display 
    Return: Python {text}
    """
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def display_integer(n):
    """
    The function display 
    “n is a number” only if n is an integer
    
    Keyword arguments:
    n -- The number to display
    Return: n
    """
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """
    The function displays an html page with the number n
    inside the <h1> tag </h1>
    
    Keyword arguments:
    n -- The number to display
    """
    # The render_template() is used to render an html template
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_and_even(n):
    """
    Displays a html page only if n is an integer
    
    Keyword arguments:
    argument -- The number to display
    Return: a html page
    """
    try:
        if n % 2 == 0:
            result = 'even'
        else:
            result = 'odd'
    except ValueError:
         return render_template('6-number_odd_or_even.html', n=n, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')