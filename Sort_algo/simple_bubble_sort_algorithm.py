# Bubble sort
def bubble_sort(arr):
    for nums in range(len(arr)-1, 0, -1):
        for x in range(nums):
            if arr[x] > arr[x + 1]:
                temp_num = arr[x]
                arr[x] = arr[x + 1]
                arr[x + 1] = temp_num

sort_me = [15, 9, 1, 15, 68, 1, 22, 3, 0, 5]

bubble_sort(sort_me)
print(sort_me)
