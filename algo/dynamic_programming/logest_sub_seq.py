"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

So a string of length n has 2^n different possible subsequences.

Optimal Substructure:
Let arr[0..n-1] be the input array and L(i) be the length of the LCS ending at index i such that arr[i] is the last element of the LCS.
Then, L(i) can be recursively written as:
L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
L(i) = 1, if no such j exists.
To find the LCS for a given array, we need to return max(L(i)) where 0 < i < n.
Thus, we see the LCS problem satisfies the optimal substructure property as the main problem can be solved using the solutions to the subproblems.

"""

from timeit import timeit

def lcs_dp(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in xrange(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0;
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1);
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n));


if __name__ == "__main__":

    # Driver program to test the above function
    X = "AGGTAB"
    Y = "GXTXAYB"

    print "Length of LCS(DP) is ", lcs_dp(X, Y)
    print "Length of LCS(Naive) is ", lcs(X, Y, len(X), len(Y))

    #timeit(lcs_dp, X, Y)
    #timeit(lcs, X, Y, len(X), len(Y))
