
def binary_search(input, element, start, end):

    if not (input and start <= end):
        return None

    middle = start + (end-start)/2
    if input[middle] == element:
        return middle
    elif input[middle] < element:
        return binary_search(input, element, middle+1, end)
    else:
        return binary_search(input, element, start, middle-1)

if __name__ == "__main__":

    input_arr = [-45, -10, -1, 0, 2, 4, 5, 8, 12, 32]
    element = 32
    print "Searching for: ", element
    print "Found %s at: %s"%(element, binary_search(input_arr, element, 0, len(input_arr)-1))
