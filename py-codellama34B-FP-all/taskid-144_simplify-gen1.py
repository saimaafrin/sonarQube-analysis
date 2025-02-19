def simplify(x: str, n: str) -> bool:
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    >>> simplify('1/5', '5/1')
    True
    >>> simplify('1/6', '2/1')
    False
    >>> simplify('7/10', '10/2')
    False
    """


    def lcm(x: int, y: int) -> int:
        if x > y:
            greater = x
        else:
            greater = y

        while True:
            if (greater % x == 0) and (greater % y == 0):
                lcm = greater
                break
            greater += 1

        return lcm

    num1, den1 = x.split("/")
    num2, den2 = n.split("/")

    num1 = int(num1)
    den1 = int(den1)
    num2 = int(num2)
    den2 = int(den2)

    lcm_val = lcm(den1, den2)
    num1_val = num1 * int(lcm_val / den1)
    num2_val = num2 * int(lcm_val / den2)

    if (num1_val * num2_val) % lcm_val == 0:
        return True
    else:
        return False
