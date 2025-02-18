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

    # 2 cars collide if they are at the same distance
    # 1 distance is a distance between two cars
    # So, there are 2 * (n - 1) distances
    # Each distance has 2^n possible positions
    # => There are 2^n * (n - 1) possible collisions
    # => There are 2^n * (n - 1) - 1 possible collisions without the one that happens when they are at the same distance
    # => There is 1 possible collision with the case where they are at the same distance
    return 2 ** n * (n - 1) - 1 + 1
