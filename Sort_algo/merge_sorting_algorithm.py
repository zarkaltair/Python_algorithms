# merge sort
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]
    merge_sort(left_part)
    merge_sort(right_part)
    i = j = k = 0
    while i < len(left_part) or j < len(right_part):
        if i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
        elif i < len(left_part):
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

sort_me = [15, 9, 1, 15, 68, 1, 22, 3, 0, 5]

merge_sort(sort_me)
print(sort_me)
