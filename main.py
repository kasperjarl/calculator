print("Hello there! \nI'm Cal the calculator. \nWhat's your name?\n")
name = input()
print(f"Hello {name}. \nWhat do you want to calculate?\n type '+' for addition\n type '-' for subtraction\n type '*' for multiplication\n type '/' for divison")

type = input("pick one: ")
number_one = 1
number_two = 2

def calculator(type, number_one: int, number_two: int):
    allowd = ['+', '-', '*', '/']
    if type not in allowd:
        return "You need to pick one of these: '+', '-', '*', '/' "

    elif type == '+':
        return number_one + number_two
    
print(calculator(type, number_one, number_two))