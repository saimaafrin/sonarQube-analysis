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
        return 1

    # for the first car, we can observe that there is a collision only if n % 2 == 1
    # because each car will collide with the following car (as they are driving
    # in the same direction)
    count = int(n % 2 == 1)

    # now consider the first and the last cars. these will collide if n is even
    count += int(n % 2 == 0)

    # consider the first, the last and the middle cars.
    # these will collide if n > 2 and the middle car is in the middle of the
    # first and the last car (if n is even).
    if n > 2:
        count += int((n % 2 == 0) and (n // 2 > 1))

    return count
