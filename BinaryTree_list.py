def binary_tree(r):
    '''Create a Tree with a root node and two empty sublists.'''
    return [r, [], []]

def insert_left(root, new_branch):
    t = root.pop(1)

    # t is not empty, we need to keep track of it and push it
    # down the tree as the left child of the list we are adding.
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    t = root.pop(2)

    # t is not empty, we need to keep track of it and push it
    # down the tree as the left child of the list we are adding.
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

if __name__ == '__main__':
    r = binary_tree(3)
    print(r)
    insert_left(r, 4)
    print(r)
    insert_left(r, 5)
    insert_right(r, 6)
    insert_right(r, 7)
    print(r)
    l = get_left_child(r)
    print(l)

    set_root_val(l, 9)
    print(r)
    insert_left(l, 11)
    print(r)
    print(get_right_child(get_right_child(r)))