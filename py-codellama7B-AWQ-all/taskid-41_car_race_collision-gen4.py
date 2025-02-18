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

    def n_car_positions(n: int) -> int:
        return int((n**2 - 1) / 2)

    def collisions(n: int) -> int:
        """
        This function calculates the number of collisions that occur in
        an infinitely long line given a set of n cars driving in one direction.
        """
        assert n > 0

        if n == 1:
            return 0

        collisions = 0

        for i in range(1, n):
            collisions += n_car_positions(i) * n_car_positions(n - i)

        return collisions

    return collisions(n) * 2
