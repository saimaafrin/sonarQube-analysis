def fib4(n: int) -> int:
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """

    # This is an implementation using a recursive approach to computing the n-th element of the fib4 sequence.
    # The fib4 sequence can be computed by a combination of the previous elements, so this implementation
    # uses recursion to compute the n-th element of the sequence.
    # The base cases are when n is 0, 1, 2, 3 or 4, in which case the result is simply the value of n.
    # Otherwise, the result is the sum of the previous elements.

    # There is a more efficient approach, which involves memoizing the previous values of the sequence.  That is,
    # instead of recomputing the value of fib4(n-1) every time we need it, we compute it once and store the value
    # in a dictionary.  This approach is faster.  The memoization dictionary is defined below, but it is not
    # returned by the function.
    fib4_memoization_dict = {0: 0, 1: 0, 2: 2, 3: 0, 4: 2}

    if n in fib4_memoization_dict:
        return fib4_memoization_dict[n]
    else:
        result = fib4_memoization_dict[n - 1] + fib4_memoization_dict[n - 2] + \
                 fib4_memoization_dict[n - 3] + fib4_memoization_dict[n - 4]
        fib4_memoization_dict[n] = result
        return result
