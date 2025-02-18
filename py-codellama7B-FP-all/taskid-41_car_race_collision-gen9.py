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

    # 1st, we'll find the maximum distance between two cars that can
    # hit each other (assuming the cars are perfectly sturdy and that
    # all cars move in the same speed)
    maximum_distance_between_hitting_cars = (2 * n) - 2
    # 2nd, we'll find the number of times each car will reach the position
    # of another car that is at maximum distance away
    number_of_repeats = n * maximum_distance_between_hitting_cars
    # 3rd, we'll find the number of times each car will pass over
    # another car that is at maximum distance away
    number_of_passes = n * (maximum_distance_between_hitting_cars + 1)
    # 4th, we'll return the result
    return number_of_repeats - number_of_passes
