def insertion_sort(a_list):
    '''把前n位排好再往后走'''
    for position in range(len(a_list)-1):
        while position >= 0 and a_list[position] > a_list[position+1]:
            a_list[position], a_list[position+1] = a_list[position+1], a_list[position]
            position -= 1

if __name__ == '__main__':
    a_list = [1, 2, 3, 4, 5, 6, 8, 32, 11, 24, 21, 23, 54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(a_list)
    print(a_list)