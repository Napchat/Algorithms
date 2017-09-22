def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        print('After increments of size', sublist_count, 
              'The list is', a_list)
        sublist_count = sublist_count // 2

'''def gap_insertion_sort(a_list, start, gap):
    for i in range(start+gap, len(a_list), gap):
        position = i
        while position >= gap and a_list[position-gap] > a_list[position]:
            a_list[position-gap], a_list[position] = a_list[position], a_list[position-gap]
            position = position - gap'''

def gap_insertion_sort(a_list, start, gap):
    """就是一个插入排序"""
    for i in range(start, len(a_list)-gap, gap):
        position = i
        while position >= start and a_list[position] > a_list[position+gap]:
            a_list[position+gap], a_list[position] = a_list[position], a_list[position+gap]
            position = position - gap

if __name__ == '__main__':
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(a_list)
    print(a_list)