# heap sort
def heapify(arr, n, i):
    # init largest as root
    largest = i
    # left
    l = 2 * i + 1
    # right
    r = 2 * i + 2

    # see if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # see if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # change root, if need
    if largest != i:
        # swap
        arr[i], arr[largest] = arr[largest], arr[i]

        # heapify the root
        heapify(arr, n, largest)


# main sort func
def heap_sort(arr):
    n = len(arr)

    # build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # one by one extract el
    for i in range(n-1, 0, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


sort_me = [15, 9, 1, 15, 68, 1, 22, 3, 0, 5]

heap_sort(sort_me)
print(sort_me)
