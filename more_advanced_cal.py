# this calculator must be able to take string like this: "(2 + 2) * (2 - 4) / 8 - 3"
# and support the following operations +, -, *, /


class Calculator:
    def __init__(self):
        print("Hello I'm the advanced calculator.\nYou can use these operations: +, -, *, /. \nInput the entire math problem in one go ")
        self.math_problem = input()            
        self.allowed_ops = ['+','-','*','/']
        self.nums = ['1','2','3','4','5','6','7','8','9']
        self.numbers = []
        self.ops = []
        print(f"Let's solve the problem: {self.math_problem}")
        print(self.problem_cleaning)
        
    def problem_cleaning(self):
        # what if we make use of two stacks: one for numbers and one for operations
        # --> What do we do when the number is more than one diget? Then we can't use for char in string.
        # --> What do we do with 12.241? The "dot"
        ops = []
        numbers = []

        for char in self.math_problem:
            print(char)
            if char in self.allowed_ops:
                ops.append(char)
            elif char in self.nums:
                numbers.append(char)

    def __repr__(self) -> str:
        return f"ops: {self.ops}\nnumbers: {self.numbers}"

print(Calculator())