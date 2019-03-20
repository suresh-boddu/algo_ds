"""
Sum of average of all subsets
Given an array arr of N integer elements, the task is to find sum of average of all subsets of this array.

Input  : arr[] = [2, 3, 5]
Output : 23.33
Explanation : Subsets with their average are,
[2]        average = 2/1 = 2
[3]        average = 3/1 = 3
[5]        average = 5/1 = 5
[2, 3]        average = (2+3)/2 = 2.5
[2, 5]        average = (2+5)/2 = 3.5
[3, 5]        average = (3+5)/2 = 4
[2, 3, 5]    average = (2+3+5)/3 = 3.33

Sum of average of all subset is,
2 + 3 + 5 + 2.5 + 3.5 + 4 + 3.33 = 23.33

Idea:

arr = [a0, a1, a2, a3]
sum of average =
a0/1 + a1/1 + a2/2 + a3/1 +
(a0+a1)/2 + (a0+a2)/2 + (a0+a3)/2 + (a1+a2)/2 +
 (a1+a3)/2 + (a2+a3)/2 +
(a0+a1+a2)/3 + (a0+a2+a3)/3 + (a0+a1+a3)/3 +
 (a1+a2+a3)/3 +
(a0+a1+a2+a3)/4

If S = (a0+a1+a2+a3), then above expression
can be rearranged as below,
sum of average = (S)/1 + (3*S)/2 + (3*S)/3 + (S)/4
Where the coefficient with numerators can be explained as follows, suppose we are iterating over subsets with K elements then denominator
will be K and numerator will be r*S, where r denotes number of times a particular array element will be added while iterating over subsets of same size.
By inspection we can see that r will be nCr(N-1, n-1) because after placing one element in summation, we need to choose n-1 elements from N-1
elements so each element will have a frequency of nCr(N-1, n-1) while considering subsets of same size, as all elements are taking part in summation
equal number of times, this will the frequency of S also and will be the numerator in final expression.
"""

from binomial_coefficient import get_binomial_coefficient_memoize


def sum_avg_all_subsets(input_arr):
    """

    :param input_arr:
    :return:
    """

    if not input_arr:
        return 0

    size = len(input_arr)
    arr_total = sum(input_arr)
    total = 0.0
    for num in range(1, size+1):
        bc = get_binomial_coefficient_memoize(size-1, num-1)
        total += (bc*arr_total)/num

    return total


if __name__ == "__main__":
    input_arr = [2, 3, 5, 7]
    print "Sum of average of all numbers in all sunsets is: %f"%sum_avg_all_subsets(input_arr)