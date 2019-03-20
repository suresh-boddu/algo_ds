"""
Dynamic Programming (DP) is an algorithmic technique for solving an optimization problem by breaking it down into
simpler subproblems and utilizing the fact that the optimal solution to the overall problem depends upon the optimal solution to its subproblems.

Characteristics of Dynamic Programming
Before moving on to understand different methods of solving a DP problem, lets first take a look at what are the characteristics
of a problem that tells us that we can apply DP to solve it.

1. Overlapping Subproblems
Subproblems are smaller versions of the original problem. Any problem has overlapping sub-problems if finding its solution
involves solving the same subproblem multiple times. Take the example of the Fibonacci numbers; to find the fib(4),
we need to break it down into the following sub-problems. We can clearly see the overlapping subproblem pattern here,
as fib(2) has been called twice and fib(1) has been called three times.

2. Optimal Substructure Property
Any problem has optimal substructure property if its overall optimal solution can be constructed from the optimal
solutions of its subproblems. For Fibonacci numbers, as we know,

Fib(n) = Fib(n-1) + Fib(n-2)

Dynamic Programming Methods
DP offers two methods to solve a problem.

1. Top-down with Memoization
In this approach, we try to solve the bigger problem by recursively finding the solution to smaller sub-problems.
Whenever we solve a sub-problem, we cache its result so that we dont end up solving it repeatedly if its called multiple times.
Instead, we can just return the saved result. This technique of storing the results of already solved subproblems is called Memoization.

2. Bottom-up with Tabulation
Tabulation is the opposite of the top-down approach and avoids recursion. In this approach, we solve the problem bottom-up
(i.e. by solving all the related sub-problems first). This is typically done by filling up an n-dimensional table.
Based on the results in the table, the solution to the top/original problem is then computed.

Tabulation is the opposite of Memoization, as in Memoization we solve the problem and maintain a map of already solved sub-problems.
In other words, in memoization, we do it top-down in the sense that we solve the top problem first (which typically recurses down to solve the sub-problems).

"""