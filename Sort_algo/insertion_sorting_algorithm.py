# Insertion sort
def insertion_sort(arr):
    for x in range(len(arr)):
        cursor = arr[x]
        pos = x
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cursor
    return arr

sort_me = [15, 9, 1, 15, 68, 1, 22, 3, 0, 5]

insertion_sort(sort_me)
print(sort_me)
