from Stack import Stack

def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split(' ')

    for token in token_list:
        try:
            operand_stack.push(int(token))
        except ValueError:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()

def do_math(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2

if __name__ == '__main__':
    print(postfix_eval('32 8 + 3 2 + /'))