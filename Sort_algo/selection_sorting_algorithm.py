# selection sort
def selection_sort(arr):
    # traverse through all arr el
    for i in range(len(arr)):
        # find the min el in arr
        min_ind = i
        for j in range(i+1, len(arr)):
            if arr[min_ind] > arr[j]:
                min_ind = j

        # swap the found min el with the first el
        arr[i], arr[min_ind] = arr[min_ind], arr[i]


sort_me = [15, 9, 1, 15, 68, 1, 22, 3, 0, 5]

selection_sort(sort_me)
print(sort_me)
