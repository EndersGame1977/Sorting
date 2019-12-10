# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(a_array, b_array):
    c = []
    a_index, b_index = 0, 0
    while a_index < len(a_array) and b_index < len(b_array):
        if a_array[a_index] < b_array[b_index]:
            c.append(a_array[a_index])
            a_index += 1
        else:
            c.append(b_array[b_index])
            b_index += 1
    if a_index == len(a_array):
        c.extend(b_array[b_index:])
    else:
        c.extend(a_array[a_index:])
    return c


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    left, right = merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
