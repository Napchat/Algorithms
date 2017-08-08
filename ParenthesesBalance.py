from Stack import Stack

def matches(open_par, end_par):
    opens = '[({'
    ends = '])}'
    return opens.index(open_par) == ends.index(end_par)

def par_cheker(symbol_string):
    symbol_stack = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced: 
        symbol = symbol_string[index]
        if symbol in '[({':
            symbol_stack.push(symbol)
        elif symbol_stack.is_empty():
            balanced = False
        else:
            top = symbol_stack.pop()
            if not matches(top, symbol):
                balanced = False

        index = index + 1

    if balanced and symbol_stack.is_empty():
        return True
    return False

if __name__ == '__main__':
    print(par_cheker('(({[()]})'))