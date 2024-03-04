import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]

def calculate(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

def evaluate_expression(expression):
    stack = Stack()
    for char in reversed(expression):
        if char.isdigit():
            stack.push(int(char))
        elif char in '+-*/':
            operand1 = stack.pop() # remove and return value from top of the stack
            operand2 = stack.pop()
            result = calculate(char, operand1, operand2) # calculate the result from stack
            stack.push(result)
    return stack.pop()

if __name__ == "__main__":
    expression = sys.argv[1] 
    print(evaluate_expression(expression))