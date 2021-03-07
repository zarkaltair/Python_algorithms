# quick sort
def partition(arr, low, high):
    # index of smaller element
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        # if currnet el is smaller than or equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller el
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is a partition index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # separately sort el before partition and after partition
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


sort_me = [15, 9, 1, 15, 68, 1, 22, 3, 0, 5]

n = len(sort_me)
quick_sort(sort_me, 0, n-1)
print(sort_me)



from random import randint

def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

sort_me = [15, 9, 1, 15, 68, 1, 22, 3, 0, 5]

print(quicksort(sort_me))
