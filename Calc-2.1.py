from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def my_form_post():

    while True:
        try:
            a = float(request.form['a'])
            break
        except ValueError:
            return "Man, first number is not a number, c'mon!"

    while True:
        try:
            b = float(request.form['b'])
            break
        except ValueError:
            return "Man, second is not a number, c'mon!"

    operations_list = ["+", "-", "*", "/"]
    while True:
        operation = request.form['operation']
        if operation in operations_list:
            break
        else:
            return "You can only put +, -, * or /"

    if operation == "/" and b == 0:
        return "Dafuq, do you want to divide by zero? GTFO!"

    def add(a, b):
        return a + b

    def multiply(a, b):
        return a - b

    def subtract(a, b):
        return a - b

    def divide(a, b):
        return a / b

    functions_list = [add, subtract, multiply, divide]
    action = dict(zip(operations_list, functions_list))

    result = action[operation](a, b)

    return str(result)

if __name__ == '__main__':
    app.run()
