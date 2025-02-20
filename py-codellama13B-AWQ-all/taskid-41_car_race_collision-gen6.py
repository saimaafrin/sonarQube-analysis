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

    # edge case
    if n < 1:
        return 0
    # base case: 1 car
    if n == 1:
        return 0
    # base case: 2 cars
    if n == 2:
        return 1
    # base case: 3 cars
    if n == 3:
        return 2
    # recursive case
    return car_race_collision(n - 1) + car_race_collision(n - 2) + car_race_collision(n - 3)
