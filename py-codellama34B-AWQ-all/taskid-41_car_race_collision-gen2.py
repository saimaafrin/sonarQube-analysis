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


    # If there are no cars, then there cannot be any collisions
    if n == 0:
        return 0

    # If there is only one car, then there cannot be any collisions
    if n == 1:
        return 0

    # Initialize the number of collisions
    collisions = 0

    # Loop through each car in the left-to-right direction
    for i in range(0, n):

        # The current car that's moving left to right
        current_left = i + 1

        # Loop through each car in the right-to-left direction
        for j in range(n - 1, -1, -1):

            # The current car that's moving right to left
            current_right = j + 1

            # If the two cars collide, then increment the number of collisions
            if current_left == current_right:
                collisions += 1

    # Return the number of collisions
    return collisions
