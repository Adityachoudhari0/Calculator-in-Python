from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Cannot take the square root of a negative number."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data['operation']
    num1 = float(data['num1'])
    num2 = float(data.get('num2', 0))

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    elif operation == 'exponentiate':
        result = exponentiate(num1, num2)
    elif operation == 'square_root':
        result = square_root(num1)
    else:
        result = "Invalid operation"

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
