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

    if n <= 1:
        return 0
    if n == 2:
        return 1

    left_to_right_car_positions = [1] * (n - 1)
    right_to_left_car_positions = [n] * (n - 1)

    collision_counter = 0
    car_positions = left_to_right_car_positions
    for i in range(n - 1):
        car_positions = [car_positions[i - 1] + car_positions[i]]
        for j, car_position in enumerate(car_positions):
            if car_position >= n:
                collision_counter += 1
                car_positions[j] -= 2 * n
            elif car_position == 1:
                collision_counter += 1
                car_positions[j] += 2 * n

    return collision_counter
