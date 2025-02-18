def car_race_collision(n: int) -> int:
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """


    from math import gcd

    n = abs(n)
    # print(gcd(n, 2 * n - 1))
    # print(gcd(n, 2 * n - 1), n)
    # print(gcd(n, 2 * n - 1), n, n * n)

    return gcd(n, 2 * n - 1) * n * n
