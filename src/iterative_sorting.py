# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        val = arr[i]  # value at current index
        min_num = min(arr[i:])  # get min num
        idx = arr.index(min_num)  # get index of the min num
        arr[i] = min_num  # assign the value at current index to min num
        arr[idx] = val  # assign the value at i to where the min num was
    return arr


# # TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    while swapped:  # continue iterating through the array and sorting
        round_swapped = False  # set false and change it only if there's a swap
        for i in range(len(arr)-1):  # iterate though each num
            right = arr[i+1]
            left = arr[i]
            if right < left:
                arr[i] = right
                arr[i+1] = left
                round_swapped = True
        swapped = round_swapped
    return arr

    # # STRETCH: implement the Count Sort function below
    # def count_sort(arr, maximum=-1):

    #     return arr


print(bubble_sort([-2, 7, 3, -9, 5, 1, 0, 4, -6]))
