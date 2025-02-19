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

    num_collisions = 0

    left_to_right_cars = set(range(1, n + 1))
    right_to_left_cars = set(range(n, 0, -1))

    while left_to_right_cars and right_to_left_cars:
        left_to_right_car = left_to_right_cars.pop()
        right_to_left_car = right_to_left_cars.pop()

        if left_to_right_car < right_to_left_car:
            left_to_right_cars.add(left_to_right_car)
            left_to_right_cars.add(right_to_left_car)
        else:
            num_collisions += 1

    return num_collisions
