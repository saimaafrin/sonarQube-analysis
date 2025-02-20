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

    # I'm using a very simple solution
    # that is O(n^2) in terms of time.
    # It should be possible to solve it with
    # O(n) time.

    # Find all the pairs of cars that are moving towards
    # each other.
    # Then determine if any of these pairs of cars
    # collide.
    # Finally, count all the collisions.

    # Find all the pairs of cars that are moving towards
    # each other.
    i = 0
    n_pairs = 0
    while i < n:
        j = 0
        while j < n:
            if i == j:
                j += 1
                continue
            if i > j:
                n_pairs += 1
            j += 1
        i += 1

    # Determine if any of these pairs of cars
    # collide.
    # Finally, count all the collisions.
    n_collisions = 0
    i = 0
    while i < n_pairs:
        j = i + 1
        while j < n_pairs:
            if cars_collide(i, j):
                n_collisions += 1
            j += 1
        i += 1

    return n_collisions
