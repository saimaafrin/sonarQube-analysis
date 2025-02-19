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


    # initialize a hash table to store the number of collisions
    # that each car has experienced so far
    # the key is the car id and the value is the number of collisions
    collisions = {}

    # initialize a queue that stores the cars that are moving
    # right to left
    right_to_left_cars = []

    # initialize the number of collisions to 0
    total_collisions = 0

    # process each car that's moving left to right
    for i in range(n):

        # if we've processed all the cars moving right to left
        # then we can break out of the loop
        if not right_to_left_cars:
            break

        # if this car has not collided with another car before
        if i not in collisions:
            collisions[i] = 0

        # while there is a car moving right to left
        # that can collide with the current car
        while right_to_left_cars and right_to_left_cars[0] < i:
            j = right_to_left_cars.pop(0)

            # if this car has not collided with another car before
            if j not in collisions:
                collisions[j] = 0

            # if this car and the previous car moving
            # right to left have not collided before
            if collisions[j] == 0:
                # increment the number of collisions for both cars
                collisions[j] += 1
                collisions[i] += 1
                total_collisions += 1

        # enqueue the current car moving right to left
        right_to_left_cars.append(i)

    # return the number of collisions
    return total_collisions
