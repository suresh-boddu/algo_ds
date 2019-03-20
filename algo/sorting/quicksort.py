'''
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
There are many different versions of quickSort that pick pivot in different ways.

    Always pick first element as pivot.
    Always pick last element as pivot (implemented below)
    Pick a random element as pivot.
    Pick median as pivot.

The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot,
put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x.
All this should be done in linear time.

'''
def partition_pivot_last(input, start, end):
    '''
    Partition logic which considers the last element for getting pivot
    :param input:
    :param start:
    :param end:
    :return:
    '''
    pivot = end
    smaller_element_index = start-1
    for index in range(start, end):
        if input[index] < input[pivot]:
            smaller_element_index += 1
            input[index], input[smaller_element_index] = input[smaller_element_index], input[index]
            print index, smaller_element_index
    input[pivot], input[smaller_element_index+1] = input[smaller_element_index+1], input[pivot]
    return smaller_element_index+1

def partition_pivot_first(input, start, end):
    '''
    Partition logic which considers the last element for getting pivot
    :param input:
    :param start:
    :param end:
    :return:
    '''

    pivot = start
    largest_element_index = end+1

    for index in range(end, start, -1):
        if input[index] > input[pivot]:
            largest_element_index -= 1
            input[largest_element_index], input[index] = input[index], input[largest_element_index]
    input[largest_element_index-1], input[pivot] = input[pivot], input[largest_element_index-1]
    return largest_element_index-1

def partition_pivot_first1(input, start, end):

    if not input or start > end:
        return

    pivot = start
    larget_index = start + 1

    for index in range(start+1, end+1):
        pass

def partition_pivot_median(input, start, end):
    '''
    Partition logic which considers the last element for getting pivot
    :param input:
    :param start:
    :param end:
    :return:
    '''

    pivot = start
    largest_element_index = end+1

    for index in range(end, start, -1):
        if input[index] > input[pivot]:
            largest_element_index -= 1
            input[largest_element_index], input[index] = input[index], input[largest_element_index]
    input[largest_element_index-1], input[pivot] = input[pivot], input[largest_element_index-1]
    return largest_element_index-1

def quicksort(input, start, end):

    if not (input and start<end):
        return

    #pivot = partition_pivot_last(input, start, end)
    pivot = partition_pivot_first(input, start, end)
    quicksort(input, start, pivot-1)
    quicksort(input, pivot+1, end)


if __name__ == "__main__":

    input_arr = [12, 4, 2, 8, -10, 5, 32, -1, 0, -45]
    print "Before Sorting: " + str(input_arr)
    quicksort(input_arr, 0, len(input_arr)-1)
    print "After Sorting: " + str(input_arr)
