"""
Problem Statement
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

Example 1:

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
Example 2:

Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
Example 3:

Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal sum.

Same as max_sum_inc_sub_sequence problem excepts that instead of counting the longest sub sequence we need to return true/false.
"""


def equal_sum_array_split(input, sum, index):
    """

    :param input:
    :param sum:
    :param index:
    :return:
    """

    if sum == 0:
        return True

    if index < 0 or not input or index >= len(input):
        return False

    result_with_curr_index = False
    if input[index] <= sum:
        result_with_curr_index = equal_sum_array_split(input, sum-input[index], index+1)
        return True

    result_without_curr_index = equal_sum_array_split(input, sum-input[index], index+1)
    return result_without_curr_index

def can_split_equal(input):
    """

    :param input:
    :return:
    """

    if not input:
        return False

    total_sum = sum(input)
    if total_sum%2 != 0:
        return False

    return equal_sum_array_split(input, total_sum/2, 0)


if __name__ == "__main__":

    print can_split_equal([1, 2, 3, 4])
    print can_split_equal([1, 1, 3, 4, 7])
    print can_split_equal([2, 3, 4, 6])
    print can_split_equal(list())


