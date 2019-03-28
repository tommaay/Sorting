# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)  # returns a length number
    merged_arr = [0] * elements
    a = 0
    b = 0
    for i in range(0, elements):
        if a == len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b == len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# print(merge([1, 2, 5, 10], [3, 4, 7, 8]))

# # TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    length = len(arr)
    mid = length // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7, 10]))


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
