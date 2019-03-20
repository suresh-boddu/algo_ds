
def pivot_end(input, start, end):

    pivot = input[end]
    swap_index = start-1

    for index in range(start, end):
        if input[index] <= pivot:
            swap_index += 1
            input[swap_index], input[index] = input[index], input[swap_index]
    input[swap_index + 1], input[end] = input[end], input[swap_index+1]
    return swap_index+1

def quicksort(input, start, end):

    if not input or start < 0 or end < 0 or start >= end:
    #if start >= end:
        return

    pivot = pivot_end(input, start, end)
    quicksort(input, start, pivot-1)
    quicksort(input, pivot, end)

if __name__ == "__main__":

    input_arr = [12, 4, 2, 8, -10, 5, 32, -1, 0, -45]
    print "Before Sorting: " + str(input_arr)
    #import timeit
    #timeit.timeit("quicksort([12, 4, 2, 8, -10, 5, 32, -1, 0, -45], 0, 9)", number=10)
    quicksort(input_arr, 0, len(input_arr)-1)
    print "After Sorting: " + str(input_arr)