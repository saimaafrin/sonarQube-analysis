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


    # We can assume n is even.
    n = n // 2
    left_to_right = range(n)
    right_to_left = range(n)
    left_to_right.reverse()
    right_to_left.reverse()
    c = 0
    while left_to_right and right_to_left:
        if left_to_right[0] == right_to_left[-1]:
            left_to_right.pop(0)
            right_to_left.pop()
            c += 1
        elif left_to_right[0] > right_to_left[-1]:
            right_to_left.pop()
        else:
            left_to_right.pop(0)

    return c
