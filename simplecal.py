# a really, really simple calculator 

print(f"Hello! I'm Cal the calculator. \nWhat do you want to calculate?\n\n type '+' for addition\n type '-' for subtraction\n type '*' for multiplication\n type '/' for divison\n type 'quit' to quit the calculator")

def calculator():
    allowedOps = ['+', '-', '*', '/', 'quit']
    
    type = input("\npick one: ")
    if type not in allowedOps:
        return "You need to pick one of these: '+', '-', '*', '/', 'quit' "
    if type == 'quit':
        return "bye!"

    number_one = float(input("\nenter the first number: "))

    number_two = float(input("\nenter the second number: "))


    if type == '+':
        return number_one + number_two
    
    elif type == '-':
        return number_one - number_two
    
    elif type == '*':
        return number_one * number_two
    
    elif type == '/':
        return number_one / number_two
    
    else:
        return "something went wrong"
    
print(calculator())