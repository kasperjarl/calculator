# this calculator must be able to take string like this: "(2 + 2) * (2 - 4) / 8 - 3"
# and support the following operations +, -, *, /


class Calculator:
    def __init__(self):
        print("Hello I'm the bit more advanced calculator.\nYou can use these operations: +, -, *, /. \nInput the entire math problem in one go WITH SPACES!")
        self.math_problem = str(input())            
        self.allowed_ops = ['+','-','*','/']
        # self.nums = ['1','2','3','4','5','6','7','8','9']
        self.ops = []
        print(f"Let's solve the problem: {self.math_problem}")
        self.problem_cleaning()
        # self.do_math()
        
    def problem_cleaning(self):
        # what if we make use of two stacks: one for numbers and one for operations
        # --> What do we do when the number is more than one diget? Then we can't use for char in string.
        # --> What do we do with 12.241? The "dot"
        # --> What do we do with: 2 * (3+4)?
       
        
        self.prob = self.math_problem.split()
        self.res = []
        self.res.append(self.prob[0])

        # now we need to some math with it..

    def do_math(self):
        pass

    def __repr__(self) -> str:
        return f"self.prob: {self.prob}\nself.ops: {self.res}"

print(Calculator())