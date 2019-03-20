"""
Introduction
Given the weights and profits of N items, we are asked to put these items in a knapsack which has a capacity C.
The goal is to get the maximum profit from the items in the knapsack. Each item can only be selected once, as we dont have multiple quantities of any item.

Lets take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5

Lets try to put different combinations of fruits in the knapsack, such that their total weight is not more than 5:

Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination, as it gives us the maximum profit and the total weight does not exceed the capacity.

Problem Statement
Given two integer arrays to represent weights and profits of N items, we need to find a subset of these items which will give us maximum profit
such that their cumulative weight is not more than a given number C. Each item can only be selected once, which means either we put an item in the knapsack or we skip it.

"""

import time
import array

def kanpsack_recursive(weights, profits, capacity, index):
    """

    :param weights:
    :param profits:
    :param capacity:
    :param index:
    :return:
    """

    if not (weights and profits) or capacity < 0 or len(weights) <= index or len(profits) <= index:
        return 0

    profit_with_curr_index = 0
    if weights[index] <= capacity:
        profit_with_curr_index = profits[index] + kanpsack_recursive(weights, profits, capacity-weights[index], index+1)

    profit_without_curr_index = kanpsack_recursive(weights, profits, capacity, index+1)
    return max(profit_with_curr_index, profit_without_curr_index)


def knapsack_bruteforce(weights, profits, capacity):
    """
    A basic brute-force solution could be to try all combinations of the given items (as we did above), allowing us to choose the one with maximum profit
    and a weight that doesnt exceed C. Take the example of four items (A, B, C, and D), as shown in the diagram below. To try all the combinations, our algorithm will look like:

    for each item i
      create a new set which INCLUDES item i if the total weight does not exceed the capacity, and
         recursively process the remaining capacity and items
      create a new set WITHOUT item i, and recursively process the remaining items

    return the set from the above two sets with higher profit
    :param weights:
    :param profits:
    :param capacity:
    :return:
    """

    return kanpsack_recursive(weights, profits, capacity, 0)

def knapsack_memoize(memoize, weights, profits, capacity, index):
    """

    :param memoize:
    :param weights:
    :param profits:
    :param capacity:
    :param index:
    :return:
    """

    if not (weights and profits) or capacity < 0 or len(weights) <= index or len(profits) <= index:
        return 0

    if memoize[index][capacity]:
        return memoize[index][capacity]

    profit_with_curr_index = 0
    if weights[index] <= capacity:
        profit_with_curr_index = profits[index] + kanpsack_recursive(weights, profits, capacity-weights[index], index+1)

    profit_without_curr_index = kanpsack_recursive(weights, profits, capacity, index+1)
    memoize[index][capacity] = max(profit_with_curr_index, profit_without_curr_index)

    return memoize[index][capacity]

def knapsack_memoization(weights, profits, capacity):
    """

    :param weights:
    :param profits:
    :param capacity:
    :return:
    """

    memoize = [[0 for i in range(capacity+1)] for j in range(len(weights))]
    return knapsack_memoize(memoize, weights, profits, capacity, 0)

def knapsack_tabulation(weights, profits, capacity):
    """

    :param weights:
    :param profits:
    :param capacity:
    :return:
    """

    if not (weights and profits) or capacity < 0:
        return 0

    dp = [[0 for i in range(capacity+1)] for j in range(len(weights))]

    for cap in range(0, capacity+1):
        if weights[0] <= cap:
            dp[0][cap] = profits[0]

    for index in range(1, len(weights)):
        for cap in range(1, capacity+1):
            profit_with_curr_index = 0
            profit_without_curr_index = 0
            if weights[index] <= cap:
                profit_with_curr_index = profits[index] + dp[index-1][cap-weights[index]]
            profit_without_curr_index = dp[index-1][cap]
            dp[index][cap] = max(profit_with_curr_index, profit_without_curr_index)
    #print dp
    return dp[len(weights)-1][capacity]

if __name__ == "__main__":

    profits = [1, 6, 12, 16, 2, 4, 3, 8, 5]
    weights = [2, 10, 1, 4, 8, 5, 6, 12, 9]
    capacity = 7

    start = time.time()
    result = knapsack_memoization(weights, profits, capacity)
    end = time.time()
    print "Knapsack profit of weight %d is %d in DP memoization took runtime: %f" % (capacity, result, end - start)

    start = time.time()
    result = knapsack_tabulation(weights, profits, capacity)
    end = time.time()
    print "Knapsack profit of weight %d is %d in DP tabulation took runtime: %f" % (capacity, result, end - start)

    start = time.time()
    result = knapsack_bruteforce(weights, profits, capacity)
    end = time.time()
    print "Knapsack profit of weight %d is %d in DP bruteforce took runtime: %f" % (capacity, result, end - start)