from InfixToPostfix import infix_to_postfix

def reverse_expr(infix_expr):
    expr_list = infix_expr.split()
    n = 0
    for token in expr_list:
        if token == '(':
            expr_list[n] = ')'
        elif token == ')':
            expr_list[n] = '('
        else:
            pass
        n += 1

    return ' '.join(expr_list[::-1])

def infix_to_prefix(infix_expr):
    rev_infix_expr = reverse_expr(infix_expr)
    return infix_to_postfix(rev_infix_expr)[::-1]

if __name__ == '__main__':
    print(infix_to_prefix('( A + B ) * ( C + D )'))
    print(infix_to_prefix(' A + B * C + D'))
