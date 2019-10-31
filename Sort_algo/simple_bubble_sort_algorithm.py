def bubble_sort(_list):
	for nums in range(len(_list)-1, 0, -1):
		for x in range(nums):
			if _list[x] > _list[x + 1]:
				temp_num = _list[x]
				_list[x] = _list[x + 1]
				_list[x + 1] = temp_num

sort_me = [15, 9, 1, 15, 68, 1, 22, 3, 0, 5]

bubble_sort(sort_me)
print(sort_me)