'''
Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.
The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one
'''


def merge(input_arr, start, middle, end):

    n1 = middle - start + 1
    n2 = end - middle

    # create temp arrays
    left_half = [0] * (n1)
    right_half = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        left_half[i] = input_arr[start + i]

    for j in range(0, n2):
        right_half[j] = input_arr[middle + 1 + j]

    #left_half = input_arr[start:middle]
    #right_half = input_arr[middle:end-1]

    li = 0
    ri = 0
    mi = start
    while li < len(left_half) and ri < len(right_half):
        if left_half[li] < right_half[ri]:
            input_arr[mi] = left_half[li]
            li += 1
        else:
            input_arr[mi] = right_half[ri]
            ri += 1
        mi += 1

    while li < len(left_half):
        input_arr[mi] = left_half[li]
        li += 1
        mi += 1

    while ri < len(right_half):
        input_arr[mi] = right_half[ri]
        ri += 1
        mi += 1


def mergesort(input_arr, start, end):

    if not (input_arr and start < end):
        return

    middle = start + (end-start)/2
    #middle = (start + (end - 1)) / 2
    mergesort(input_arr, start, middle)
    mergesort(input_arr, middle+1, end)
    merge(input_arr, start, middle, end)


if __name__ == "__main__":

    input_arr = [12, 4, 2, 8, -10, 5, 32, -1, 0, -45]
    size = len(input_arr)
    print "Before Sorting: " + str(input_arr)
    mergesort(input_arr, 0, size-1)
    print "After Sorting: " + str(input_arr)