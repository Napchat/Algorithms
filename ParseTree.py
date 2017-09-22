import operator

from Stack import Stack
from BinaryTree_nodes_references import BinaryTree

def build_parse_tree(fp_exp):
    fp_list = fp_exp.strip().split()

    # Stack用于保存父结点
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fp_list:
        if i == '(':
            current_tree.insert_left(' ')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i == ' ':
            pass
        elif i not in ['+', '-', '*', '/', ')']:
            # 数字
            current_tree.set_root_val(int(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree

def evaluate(parse_tree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}
    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()

    if left and right:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left), evaluate(right))
    else:
        return parse_tree.get_root_val()

def postorder_eval(tree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postorder_eval(tree.get_left_child)
        res2 = postorder_eval(tree.get_right_child)
        if res1 and res2:
            return opers[tree.get_root_val()](res1, res2)
        else:
            return tree.get_root_val()

def print_exp(tree):
    str_val = ''
    if tree:
        str_val = '(' + print_exp(tree.get_left_child())
        str_val = str_val + str(tree.get_root_val())
        str_val = str_val + print_exp(tree.get_right_child()) + ')'
    return str_val

if __name__ == '__main__':
    tree = build_parse_tree('( ( 1 + 2 ) * ( 5 - 3 ) - ( 9 - 6 ) )')
    print(print_exp(tree))
    print(evaluate(tree))