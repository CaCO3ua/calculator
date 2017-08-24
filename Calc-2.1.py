from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("index.html")


@app.route('/answer/', methods=['POST'])
def answer():

    try:
        first_operand = float(request.form['first_operand'])
    except ValueError:
        return "Man, first number is not a number, c'mon!"

    try:
        second_operand = float(request.form['second_operand'])
    except ValueError:
        return "Man, second number is not a number, c'mon!"

    operations_list = ["+", "-", "*", "/"]
    operation = request.form['operation']
    if operation not in operations_list:
        return "You can only put +, -, * or /"

    def add(first_operand, second_operand):
        return first_operand + second_operand

    def multiply(first_operand, second_operand):
        return first_operand - second_operand

    def subtract(first_operand, second_operand):
        return first_operand - second_operand

    def divide(first_operand, second_operand):
        try:
            return first_operand / second_operand
        except ZeroDivisionError:
            return "Dafuq, do you want to divide by zero? GTFO!"

    functions_list = [add, subtract, multiply, divide]
    action = dict(zip(operations_list, functions_list))

    result = action[operation](first_operand, second_operand)

    return str(result)

if __name__ == '__main__':
    app.run()
