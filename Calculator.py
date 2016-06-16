while 1:
    try:
        a = float(input("Type in the first number, please:\n"))
        break
    except ValueError:
        print ("Man, that is not a number, c'mon!")

while 1:
    try:
        b = float(input("Type in the second number, please:\n"))
        break
    except ValueError:
        print ("Man, that is not a number, c'mon!")

while 1:
    operation = (input("Type in the operation, please (+, -, *, /):\n"))
    if operation == "+" or operation == "-" or operation == "*" or operation == "/":    break
    else:
        print ("You can only put +, -, * or /")        

def add(a, b):
    return a + b
    
def multiply(a, b):
    return a - b
    
def subtract(a, b):
    return a - b
    
def divide(a, b):
    return a / b
    
action = {
	"+" : add,
	"*" : multiply,
	"-" : subtract,
	"/" : divide
	}
	
result = action [operation](a,b)

print ("The answer is: " + result)
