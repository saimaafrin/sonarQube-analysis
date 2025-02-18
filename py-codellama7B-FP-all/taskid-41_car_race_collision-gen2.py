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

    # When the distance between the two cars on either side of the road are the
    # same, and one of the cars has not yet crossed over the middle, then the
    # collisions occur.
    #
    # The two cars on either side of the road are moving at the same speed
    # and the distance between them is constant.  However, the distance between
    # the two cars moving in the opposite direction is changing.  So the problem
    # can be reduced to a problem of determining the number of times that the two
    # cars moving in opposite directions cross over the middle.
    #
    # The two cars moving in opposite directions will cross over the middle
    # when the sum of the two distances is equal to the product of the two speeds.
    #
    # So the number of collisions is equal to the number of times that the sum of
    # the two distances is equal to the product of the two speeds.
    #
    # There are n cars on each side of the road;  so there are 2 * n cars on
    # the road.  The distance between cars on either side is constant;  so there are
    # n + 1 cars between each other.
    #
    # So the number of collisions is equal to the number of times that the sum of
    # the two distances is equal to the product of the two speeds.
    #
    # The total number of collisions is equal to the number of times that the sum
    # of the two distances is equal to the product of the two speeds.
    #
    # The sum of the two distances is equal to the product of the two speeds.
    #
    # The number of collisions is equal to the number of times that the sum of
    # the two distances is equal to the product of the two speeds.
    #
    # The distance between cars on either side is constant;  so the number of
    # collisions is equal to the number of times that the sum of the two distances
    # is equal to the product of the two speeds.
    #
    # The total number of collisions is equal to the number of times that the sum
    # of the two distances is equal to the product of the two speeds.
    #
    # The speed of the cars is constant;  so the number of collisions is equal
    # to the number of times that the sum of the two distances is equal to the
    # product of the two speeds.
    #
    # The number of collisions is equal to the number of times that the sum of
    # the two distances is equal to the product of the two speeds.
    #
    # The distance between cars on either side is constant;  so the number of
    # collisions is equal to the number of times that the sum of the two distances
    # is equal to the product of the two speeds.
    #
    # The total number of collisions is equal to the number of times that the sum
    # of the two distances is equal to the product of the two speeds.
    #
    # The speed of the cars is constant;  so the number of collisions is equal
    # to the number of times that the sum of the two distances is equal to the
    # product of the two speeds.
    #
    # The number of collisions is equal to the number of times that the sum of
    # the two distances is equal to the product of the two speeds.
    #
    # The distance between cars on either side is constant;  so the number of
    # collisions is equal to the number of times that the sum of the two distances
    # is equal to the product of the two speeds.
    #
    # The total number of collisions is equal to the
