import sys
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def evaluate(self):
        if isinstance(self.data, int):
            return self.data
        left_val = self.left.evaluate() if self.left else None
        right_val = self.right.evaluate() if self.right else None
        return self.apply_operation(left_val, right_val)

    def apply_operation(self, left, right):
        if self.data == '+': return left + right
        elif self.data == '-': return left - right
        elif self.data == '*': return left * right
        elif self.data == '/': return left / right
        return 0

def build_expression_tree(tokens):
    def parse_expression(tokens):
        if not tokens:
            return None
        if tokens[0] == '(' and tokens[-1] == ')':
            tokens = tokens[1:-1]
        
        lowest_precedence = float('inf')
        operator_position = -1
        parentheses_count = 0

        for i in range(len(tokens) - 1, -1, -1):
            token = tokens[i]

            if token == ')':
                parentheses_count += 1
            elif token == '(':
                parentheses_count -= 1
            elif parentheses_count == 0 and token in {'+', '-', '*', '/'}:
                precedence = {'+': 1, '-': 1, '*': 2, '/': 2}[token]
                if precedence <= lowest_precedence:
                    lowest_precedence = precedence
                    operator_position = i

        if operator_position != -1:
            root = Node(tokens[operator_position])
            root.left = parse_expression(tokens[:operator_position])
            root.right = parse_expression(tokens[operator_position + 1:])
            return root
        else:
            if tokens[0].isdigit():
                return Node(int(tokens[0]))
            else:
                return parse_expression(tokens[1:-1])  # Handle single number inside parentheses

    return parse_expression(tokens)

def main(expression):
    tokens = expression.split()
    root = build_expression_tree(tokens)
    result = root.evaluate()
    print(int(result))

if __name__ == "__main__":
    expression = sys.argv[1]
    main(expression)
