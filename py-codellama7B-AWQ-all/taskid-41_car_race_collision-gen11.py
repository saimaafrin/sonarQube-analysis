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

    # The number of collisions.
    collisions = 0
    # The distance between the two sets of cars.
    distance = 0

    # While the two sets of cars have not collided.
    while distance < n:
        # The first car in the left-to-right set is about to move one unit to the right.
        distance += 1

        # The first car in the right-to-left set is about to move one unit to the left.
        distance -= 1

        # Increment the number of collisions.
        collisions += 1

    # Return the number of collisions.
    return collisions
