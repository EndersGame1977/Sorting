# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        leftIndex = i
        for j in range(i+1, len(arr)):
            rightIndex = j
            if arr[j] < arr[i]:
                arr[leftIndex], arr[rightIndex] = arr[rightIndex], arr[leftIndex]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        sortedIndex = i
        for j in range(0, len(arr) - 1 - sortedIndex):
            leftIndex = j
            rightIndex = j+1
            if arr[j] > arr[j+1]:
                arr[leftIndex], arr[rightIndex] = arr[rightIndex], arr[leftIndex] 
    return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr