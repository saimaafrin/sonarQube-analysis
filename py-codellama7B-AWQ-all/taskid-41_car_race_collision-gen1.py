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

    # Initialize the number of collisions.
    num_collisions = 0

    # Initialize the position of the left-to-right cars as 0.
    left_pos = [0 for _ in range(n)]

    # Initialize the position of the right-to-left cars as infinity.
    right_pos = [float('inf') for _ in range(n)]

    # Initialize the speed of the left-to-right cars as 1.
    left_speed = [1 for _ in range(n)]

    # Initialize the speed of the right-to-left cars as 1.
    right_speed = [1 for _ in range(n)]

    # Iterate through all the time steps.
    for _ in range(n):

        # Move the left-to-right cars.
        for i in range(n):
            left_pos[i] += left_speed[i]

        # Move the right-to-left cars.
        for i in range(n):
            right_pos[i] -= right_speed[i]

        # If any two cars collide, increase the number of collisions.
        for i in range(n):
            if abs(left_pos[i] - right_pos[i]) <= 1:
                num_collisions += 1

    # Return the number of collisions.
    return num_collisions
