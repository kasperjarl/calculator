# this calculator must be able to take string like this: "(2 + 2) * (2 - 4) / 8 - 3"
# and support the following operations +, -, *, /


class Calculator:
    def __init__(self):
        print("Hello I'm the bit more advanced calculator.\nYou can use these operations: +, -, *, /. \nInput the entire math problem in one go WITH SPACES!")
        self.math_problem = str(input())            
        self.allowed_ops = ['+','-','*','/']
        self.res = 0
        print(f"Let's solve the problem: {self.math_problem}")
        self.problem_cleaning()
        self.do_math()
        
    def problem_cleaning(self):
        self.operations = self.math_problem.split()
        self.res = float(self.operations[0])
        self.operations = self.operations[1:]


    def do_math(self):
        while self.operations:
            if self.operations[0] == '+':
                self.addition()
            elif self.operations[0] == '-':
                self.subtraction()
            elif self.operations[0] == '*':
                self.multiplication()
            elif self.operations[0] == '/':
                self.division()
            else:
                raise ValueError("You can only use these operations: +, -, *, /, no () and there must be spaces in between.")

    def addition(self):
        self.res += float(self.operations[1])
        self.operations = self.operations[2:]

    def subtraction(self):
        self.res -= float(self.operations[1])
        self.operations = self.operations[2:]

    def multiplication(self):
        self.res *= float(self.operations[1])
        self.operations = self.operations[2:]
    
    def division(self):
        self.res /= float(self.operations[1])
        self.operations = self.operations[2:]

    def __repr__(self) -> str:
        return f"self.operations: {self.operations}\nself.res: {self.res}"

print(Calculator())