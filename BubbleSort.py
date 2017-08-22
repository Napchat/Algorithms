from timeit import Timer

def bubble_sort(list):
    '''第一层循环每一次都将最大的数排到最后面
    冒泡是最没有效率的排序'''
    for pass_num in range(len(list)-1, 0, -1):
        for i in range(pass_num):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]

def short_bubble_sort(list):
    '''如果没有交换发生，结束循环'''

    '''exchange = True
    pass_num = len(list)-1
    while pass_num > 0 and exchange:
        exchange = False
        for i in range(pass_num):
            if list[i] > list[i+1]:
                exchange = True
                list[i], list[i+1] = list[i+1], list[i]
        pass_num -= 1'''

    exchange = True
    for pass_num in range(len(list)-1, 0, -1):
        if exchange == False:
            break
        exchange = False
        for i in range(pass_num):
            if list[i] > list[i+1]:
                exchange = True
                list[i], list[i+1] = list[i+1], list[i]

if __name__ == '__main__':
    a_list = [1, 2, 3, 4, 5, 6, 8, 32, 11, 24, 21, 23, 54, 26, 93, 17, 77, 31, 44, 55, 20]
    t1 = Timer('short_bubble_sort(a_list)', 'from __main__ import short_bubble_sort, a_list')
    t2 = Timer('bubble_sort(a_list)', 'from __main__ import bubble_sort, a_list')
    print(t1.timeit())
    print(t2.timeit())