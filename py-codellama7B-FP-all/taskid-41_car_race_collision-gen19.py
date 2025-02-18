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

    # We can use the fact that a car moving left to right will always collide with a car
    # moving right to left before the number of cars on the road equals n
    # Therefore, if n > (1 + sqrt(5)) / 2
    # then we can just do a modular exponentiation to find the answer
    # else we need to do a binary search on the collisions

    def mod_exp(base: int, exp: int, mod: int) -> int:
        res = 1
        while exp > 0:
            if exp % 2 == 1:
                res *= base
                res %= mod
            base *= base
            base %= mod
            exp >>= 1
        return res

    if n > (1 + sqrt(5)) / 2:
        return mod_exp(2, n, 10 ** 9 + 7)

    # Perform binary search
    lo, hi = 0, n
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if car_race_collision_helper(mid) == n:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1
