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


    # Initialize variables
    i: int = 0  # Initialize collision counter
    collisions: list[int] = []  # List of collision indices
    colliding: bool = False  # Check if colliding
    car_set_left: list[int] = []  # Cars moving left to right
    car_set_right: list[int] = []  # Cars moving right to left
    left_car: int = 0  # Car moving left to right
    right_car: int = 0  # Car moving right to left

    # Populate car set with n cars
    while i < n:
        car_set_left.append(i + 1)
        car_set_right.append(i + 1)
        i += 1

    # Loop through cars and check for collisions
    for i in car_set_left:
        for j in car_set_right:
            if i == j:
                colliding = True
                collisions.append(i)

    # Iterate through collisions and print collision
    for i in collisions:
        print(f"Collision! Cars {left_car} and {right_car}")

    return len(collisions)
