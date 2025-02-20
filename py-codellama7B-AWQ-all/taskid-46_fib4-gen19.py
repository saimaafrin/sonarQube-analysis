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

    # Write your code here
    # This is a solution that uses a list as a 'memory' to store each previous
    # value of fib4, to help keep the function from getting too large.
    # Initially, the list contains 0, 1, 2, 3 (these are the values of fib4 for 0
    # through 3).  Then, for each additional call to the function, we use the
    # previous values in the list to calculate the next value in the sequence.
    fib4_list = [0, 1, 2, 3]
    for i in range(n - 3):
        fib4_list.append(fib4_list[-1] + fib4_list[-2] + fib4_list[-3] + fib4_list[-4])
    return fib4_list[n]
