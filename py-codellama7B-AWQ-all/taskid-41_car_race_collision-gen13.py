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

    if n == 1:
        return 0

    # We consider every pair of cars that are colliding.  There are 2n such pairs.
    # We consider every possible way of a car being a part of such a pair.  There
    # are n such cars (that is, the cars that are moving left to right).  As a
    # result, we consider the number of such a car times the number of cars that
    # are moving right to left.  This is n times (n - 1) = n^2 - n.
    # Therefore, the total number of collisions is n^2 - n.
    return n * (n - 1)
