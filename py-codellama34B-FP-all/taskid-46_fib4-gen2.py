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


    first_prev = 0
    second_prev = 0
    third_prev = 2
    fourth_prev = 0

    if n <= 3:
        return third_prev

    for i in range(4, n + 1):
        current = first_prev + second_prev + third_prev + fourth_prev
        first_prev = second_prev
        second_prev = third_prev
        third_prev = fourth_prev
        fourth_prev = current

    return fourth_prev
