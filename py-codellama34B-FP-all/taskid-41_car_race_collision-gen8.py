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

    # Initialize the two sets of cars as lists
    left_to_right_cars = []
    right_to_left_cars = []
    # Initialize the number of collisions as 0
    num_collisions = 0

    # This loop runs n times
    for i in range(n):
        # Add an element to the left to right cars
        left_to_right_cars.append(i)
        # Add an element to the right to left cars
        right_to_left_cars.append(i)

    # Check for each car in the left to right cars
    for car_i in left_to_right_cars:
        # Check for each car in the right to left cars
        for car_j in right_to_left_cars:
            # Check if the distance between the cars is 0
            if car_i - car_j == 0:
                # Increment the number of collisions
                num_collisions += 1

    return num_collisions
