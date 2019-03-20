

def lss_with_given_sum(weights, profits, sum, index):
    """
    This is kind of a Knapsack problem where weights are input array elements, profits are 1 each and capacity is sum
    :param weights:
    :param profits:
    :param sum:
    :param index:
    :return:
    """

    if not (weights and profits) or index < 0 or sum < 0 or len(weights) <= index or len(profits) <= index:
        return 0

    len_with_curr_index = 0
    if weights[index] <= sum:
        len_with_curr_index = profits[index] + lss_with_given_sum(weights, profits, sum-weights[index], index + 1)

    len_without_curr_index = lss_with_given_sum(weights, profits, sum, index + 1)
    return max(len_with_curr_index, len_without_curr_index)

if __name__ == "__main__":

    sum = 11
    input_arr = [45, 10, 1, 3, 4, 8, 5, 6, 12, 27]
    value = lss_with_given_sum(input_arr, [1]*len(input_arr), sum, 0)
    print "LSS value for sum : %d is : %d"%(sum, value)