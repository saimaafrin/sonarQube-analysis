def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """


    if n <= 0:
        return 2
    elif n == 1:
        return 3
    else:
        prime_list = [3, 5, 13]
        current_number = 13
        count = 3
        while count < n:
            new_number = prime_list[count - 1] + prime_list[count - 2]
            if is_prime(new_number):
                prime_list.append(new_number)
                current_number = new_number
                count += 1
            else:
                current_number += 2
        return current_number
