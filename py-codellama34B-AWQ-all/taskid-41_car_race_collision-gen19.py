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


    def collision(car_left, car_right) -> int:
        # cars are infinitesimally small, so a collision is possible if they
        # cross the axis in the same direction
        return 1 if car_left > 0 and car_right > 0 else 0

    # two sets of n cars, each with length 1
    cars_left = [1] * n
    cars_right = [1] * n

    collisions = 0
    # while there are still cars remaining on each side,
    # incrementally move the cars, comparing them against each other
    while cars_left and cars_right:
        # if both cars have a positive length,
        # then we can safely move the cars forward by one unit
        if cars_left[-1] > 0 and cars_right[0] > 0:
            # add the number of collisions that occurred
            collisions += collision(cars_left[-1], cars_right[0])

        # move the cars forward
        cars_left.append(0)
        cars_left.pop(0)
        cars_right.append(0)
        cars_right.pop(0)

    return collisions
