"""

The Longest Increasing Sub sequence (LIS) problem is to find the length of the longest sub sequence of a given sequence
such that all elements of the sub sequence are sorted in increasing order.
For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

Optimal Substructure:
Let arr[0..n-1] be the input array and L(i) be the length of the LIS ending at index i such that arr[i] is the last element of the LIS.
Then, L(i) can be recursively written as:
L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
L(i) = 1, if no such j exists.
To find the LIS for a given array, we need to return max(L(i)) where 0 < i < n.
Thus, we see the LIS problem satisfies the optimal substructure property as the main problem can be solved using solutions to subproblems.

"""

def longest_inc_sub_seq(input):

    if not input:
        return 0

    size = len(input)
    lis = [1] * size

    for outer in range(1, size):
        for inner in range(0, outer):
            if input[outer] > input[inner] and lis[inner] >= lis[outer]:
                lis[outer] = lis[inner] + 1
    return max(lis)

if __name__ == "__main__":

    #input_arr = [12, 4, 2, 8, -10, 5, 32, -1, 0, -45]
    #input_arr = [-45, -10, -1, 0, 2, 4, 5, 8, 12, 32]
    input_arr = [-45, -50, -30, -60, -35, -25, -70]
    value = longest_inc_sub_seq(input_arr)
    print "LIS value: " + str(value)
