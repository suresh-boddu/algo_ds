"""
Heap Sort Algorithm

Let us first define a Complete Binary Tree. A complete binary tree is a binary tree in which every level, except possibly the last,
is completely filled, and all nodes are as far left as possible (Source Wikipedia)

A Binary Heap is a Complete Binary Tree where items are stored in a special order such that value in a parent node is greater(or smaller) than the values in its two children nodes.
The former is called as max heap and the latter is called min heap. The heap can be represented by binary tree or array.

Since a Binary Heap is a Complete Binary Tree, it can be easily represented as array and array based representation is space efficient.
If the parent node is stored at index I, the left child can be calculated by 2 * I + 1 and right child by 2 * I + 2 (assuming the indexing starts at 0)


Heap Sort Algorithm for sorting in increasing order:
1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of tree.
3. Repeat above steps while size of heap is greater than 1.

"""

def heapify(input, size, index):
    '''
    Applying the heap properties on input array at given index.
    :param input:
    :param index:
    :return:
    '''

    if not input or index < 0:
        return

    lc_index = 2*index + 1
    rc_index = 2*index + 2
    largest_index = index

    if lc_index < size and input[lc_index] > input[index]:
        largest_index = lc_index
    if rc_index < size and input[rc_index] > input[largest_index]:
        largest_index = rc_index

    if largest_index != index:
        input[largest_index], input[index] = input[index], input[largest_index]
        heapify(input, size, largest_index)


def heapsort(input):

    '''
    heapsort algorithm
    :param input:
    :return:
    '''

    if not input:
        return

    size = len(input)
    for index in range(size/2-1, -1, -1):
        heapify(input, size, index)

    for index in range(size-1, 0, -1):
        input[0], input[index] = input[index], input[0]
        heapify(input, index, 0)


if __name__ == "__main__":

    input = [12, 4, 2, 8, -10, 5, 32, -1, 0, -45]
    print "Before Sorting: " + str(input)
    heapsort(input)
    print "After Sorting: " + str(input)