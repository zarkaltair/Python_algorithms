import random


# quick sort Hoare
def q_sort(arr):
    if len(arr) > 1:
        x = arr[random.randint(0, len(arr)-1)]
        low = [u for u in arr if u < x]
        eq = [u for u in arr if u == x]
        hi = [u for u in arr if u > x]
        arr = q_sort(low) + eq + q_sort(hi)
    return arr


sort_me = [15, 9, 1, 15, 68, 1, 22, 3, 0, 5]

sorted_me = q_sort(sort_me)
print(sorted_me)
