import time


def get_binomial_coefficient(N, R):
    """
    Function to return the Binomial Coefficient of NcR which is N!/(R! * (N-R)!)
    Idea is if NcR can be represented as C(N, R) = C(N-1, R-1) + C(N-1, R) and C(N, 0) = C(N, N) = 1
    :param N:
    :param R:
    :return:
    """

    if N == 0:
        return 0
    if R == 1:
        return N
    if R == 0 or N == R:
        return 1

    return get_binomial_coefficient(N-1, R-1) + get_binomial_coefficient(N-1, R)


def get_binomial_coefficient_memoize(N, R):
    """
    Function to return the Binomial Coefficient of NcR which is N!/(R! * (N-R)!)
    Idea is if NcR can be represented as C(N, R) = C(N-1, R-1) + C(N-1, R) and C(N, 0) = C(N, N) = 1
    :param N:
    :param R:
    :return:
    """

    if N == 0:
        return 0
    if R == 1:
        return N
    if R == 0 or N == R:
        return 1

    dp = [[0 for x in range(R + 1)] for x in range(N + 1)]
    for n in range(1, N+1):
        for r in range(min(n, R)+1):
            if r == 0 or n == r:
                dp[n][r] = 1
            else:
                dp[n][r] = dp[n-1][r-1] + dp[n-1][r]
    return dp[n][r]


if __name__ == "__main__":

    N = input()
    R = input()
    start = time.time()
    value = get_binomial_coefficient(N, R)
    end = time.time()
    print "C(%d, %d) through recursion in time(%d) is: %s"%(N, R, end-start, value)
    start = time.time()
    value = get_binomial_coefficient_memoize(N, R)
    end = time.time()
    print "C(%d, %d) through memoization in time(%d) is: %s" % (N, R, end-start, value)

