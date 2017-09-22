def selection_sort(a_list):
	'''找到最大(最小)的一个，然后放到最后(最前面)，再在剩下的数中重复该过程
	相比起冒泡法，虽然比较的次数一样，但减少了交换的次数
	'''
	for sort_num in range(0, len(a_list)-1):
		pos_of_min = sort_num
		for position in range(sort_num, len(a_list)):
			if a_list[position] < a_list[pos_of_min]:
				pos_of_min = position

		a_list[sort_num], a_list[pos_of_min] = a_list[pos_of_min], a_list[sort_num]

if __name__ == '__main__':
	a_list = [1, 2, 3, 4, 5, 6, 8, 32, 11, 24, 21, 23, 54, 26, 93, 17, 77, 31, 44, 55, 20]
	selection_sort(a_list)
	print(a_list)