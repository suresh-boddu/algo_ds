import time
import array

def fibonacci_tabulation(number):
    """

    :param number:
    :return:
    """

    if number <= 0:
        return number

    table = array.array('i', [0]*(number+1))
    table[1] = 1

    for num in range(2, number+1):
        table[num] = table[num-1] + table[num-2]

    return table[number]

def fibonacci_memoize(memoize, number):
    """

    :param memoize:
    :param number:
    :return:
    """

    if number <= 1:
        return number

    if number and memoize[number]:
        return memoize[number]

    memoize[number] = fibonacci_memoize(memoize, number - 1) + fibonacci_memoize(memoize, number - 2)
    return memoize[number]

def fibonacci_memoization(number):
    """

    :param number:
    :return:
    """

    memoize = array.array('i', [0]*(number+1))
    return fibonacci_memoize(memoize, number)

def fibonacci(number):
    """

    :param number:
    :return:
    """

    if number <= 1:
        return number

    return fibonacci(number-1) + fibonacci(number-2)

def main():

    num = 30

    start = time.time()
    result = fibonacci_memoization(num)
    end = time.time()
    print "%sth Fibonacci number (%s) DP Memoization Runtime: %f" % (num, result, end - start)

    start = time.time()
    result = fibonacci_tabulation(num)
    end = time.time()
    print "%sth Fibonacci number (%s) DP Tabulation Runtime: %f" % (num, result, end - start)

    start = time.time()
    result = fibonacci(num)
    end = time.time()
    print "%sth Fibonacci number (%s) DP plain recursion Runtime: %f" % (num, result, end - start)

if __name__ == '__main__':
    main()
