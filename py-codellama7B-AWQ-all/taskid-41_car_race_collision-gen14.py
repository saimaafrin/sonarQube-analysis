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

    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        left_to_right = 1
        right_to_left = 1
        collisions = 0

        while left_to_right < right_to_left:
            collisions += 1
            left_to_right += 2
            right_to_left += 2
        return collisions
