def insertion_sort(list_):
    for x in range(len(list_)):
        cursor = list_[x]
        pos = x
        while pos > 0 and list_[pos - 1] > cursor:
            list_[pos] = list_[pos - 1]
            pos = pos - 1
        list_[pos] = cursor
    return list_

arr = [15, 2, 4, 50, 32, 2, 0, 1, 4]
sorted = insertion_sort(arr)
print(sorted)