import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_tree(tokens):
    def helper(token_list):
        stack = []
        while token_list:
            token = token_list.pop()
            if token == ')':  # Start of a subexpression (in reverse order)
                stack.append(helper(token_list))
            elif token in '+-*/':
                right = stack.pop()
                left = stack.pop()
                node = TreeNode(token)
                node.left = left
                node.right = right
                stack.append(node)
            elif token == '(':  # End of a subexpression
                return stack.pop()  # Return the subexpression tree
            else:  # Token is a number
                stack.append(TreeNode(float(token)))
        return stack.pop()

    # Reverse the tokens for right-to-left evaluation (to mimic stack behavior correctly)
    tokens = tokens[::-1]
    return helper(tokens)

def evaluate_tree(node):
    if node.value == '+':
        return evaluate_tree(node.left) + evaluate_tree(node.right)
    elif node.value == '-':
        return evaluate_tree(node.left) - evaluate_tree(node.right)
    elif node.value == '*':
        return evaluate_tree(node.left) * evaluate_tree(node.right)
    elif node.value == '/':
        return evaluate_tree(node.left) / evaluate_tree(node.right)
    else:  # Node is a number
        return node.value

def parse_expression(expression):
    tokens = expression.split()
    return construct_tree(tokens)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py '(expression)'")
        return
    expression = sys.argv[1]
    tree = parse_expression(expression)
    result = evaluate_tree(tree)
    print(result)

if __name__ == '__main__':
    main()
