"""

Given an array A of N positive integers. Find the sum of maximum sum non-decreasing sub-sequence of the given array.
If input is: 1 101 2 3 100 4 5, there would be increasing sub-sequences: (1, 101), (1, 2, 3, 100), (1, 2, 3, 4, 5).
Among these the result would be (1, 2, 3, 100) and max sum is 106

"""


def max_increasing_sub_seq(input_list):
    """
    Idea: Create a new index_lax list by initializing with the input list at starting as the default max at each index is its value itself.
    Now, at every index starting from 1 to len(input_list)-1, we need to identify the maximum sum for any non-decreasing sub-sequence till that index
    and store those in a list against that index. Finally return the max of this new list.
    While identifying the maximum sum at an index we can look back the in to the previous indices from the current index and,
    if the value of prev index is less than current one,
        update the index_max list at current index if the sum of index_max[previous index] and value of current index is higher than the index_max[curr index]
    :param input_list:
    :return:
    """

    if not input_list:
        return None

    index_max = [ val for val in input_list]
    for val in input_list:
        index_max.append(val)

    for cur_index in range(1, len(input_list)):
        for prev_index in  range(cur_index-1, -1, -1):
            if input_list[prev_index] <= input_list[cur_index]:
                index_max[cur_index] = max (index_max[cur_index], index_max[prev_index] + input_list[cur_index])

    return max(index_max)


if __name__ == "__main__":
    print max_increasing_sub_seq([1, 101, 2, 3, 100, 4, 5])
    print max_increasing_sub_seq([1, 2, 3, 4, 5, 100, 101])
    print max_increasing_sub_seq([105, 101, 59, 42, 12, 7, 5])
    print max_increasing_sub_seq(list())