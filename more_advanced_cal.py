# I discovered "eval" ...

class Calculator:
    def __init__(self):
        print("Hello I'm the bit more advanced calculator.\nInput the entire math problem in one go: ")
        self.math_problem = str(input())

        self.res = ("Answer: " + str(eval(self.math_problem)))

    def __repr__(self) -> str:
        return f"{self.res}"

print(Calculator())