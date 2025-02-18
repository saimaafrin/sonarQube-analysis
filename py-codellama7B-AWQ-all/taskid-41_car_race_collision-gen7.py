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

    left_to_right = [0 for _ in range(n)]
    right_to_left = [0 for _ in range(n)]
    n_collisions = 0
    for _ in range(n * 2):
        left_to_right, right_to_left = right_to_left, left_to_right
        n_collisions += left_to_right.count(1) * right_to_left.count(1)
    return n_collisions
