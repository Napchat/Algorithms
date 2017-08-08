from Stack import Stack

def divide_by_base(dec_number, base):
    digits = '0123456789ABCDEF'
    rem = Stack()

    while dec_number > 0:
        rem.push(dec_number % base)
        dec_number = dec_number // base

    binary_list = []

    while not rem.is_empty():
        binary_list.append(digits[rem.pop()])

    return ''.join(binary_list)

if __name__ == '__main__':
    print(divide_by_base(42, 2))
    print(divide_by_base(255, 16))