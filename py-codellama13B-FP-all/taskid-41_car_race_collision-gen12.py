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


    # We are interested in the number of collisions, which is equal to the number
    # of pairs of cars that collide.  Since the cars are moving in opposite directions,
    # the cars that collide are those that are placed at the same index.  For example,
    # the cars that collide at index 0 are cars 0 and n-1.
    #
    # The distance between cars at index i and index j is equal to the absolute value of i-j.
    # The total number of collisions is equal to the sum of the distances between all cars
    # that collide.

    # The total number of cars is 2 * n.
    # The distance between cars at index i and index j is equal to the absolute value of i-j.
    # The total number of collisions is equal to the sum of the distances between all cars
    # that collide.

    return sum(range(n))
