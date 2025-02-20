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

    # We can represent the starting position of each car as a pair of (left, right).
    # left is the index of the leftmost car and right is the index of the rightmost car.
    # At each time step, we move the leftmost car to the right, the rightmost car to the left.
    # Each car is moved forward (or backward) in the direction it's moving.
    # Therefore, we don't need to worry about the direction of the cars.
    # This is because all cars move in the same speed.
    # Note that the cars are infinitely strong and can continue moving in their trajectory.
    # Therefore, if a car that's moving left to right hits a car that's moving right to left,
    # the cars continue moving in their trajectory as if nothing happened.
    # The number of collisions is the number of times when a car that's moving left to right
    # hits a car that's moving right to left.

    # Time complexity: O(n)
    # Space complexity: O(n)

    # We can move the leftmost car to the right, and the rightmost car to the left
    # and count the number of collisions in each time step.
    # This way, we don't need to worry about the direction of the cars.
    # This is because all cars move in the same speed.
    # Therefore, we can represent the starting position of each car as a pair of (left, right)
    # where left is the index of the leftmost car and right is the index of the rightmost car.
    # If a car that's moving left to right hits a car that's moving right to left,
    # the cars continue moving in their trajectory as if nothing happened.
    # The number of collisions is the number of times when a car that's moving left to right
    # hits a car that's moving right to left.

    # For example, if n = 5, the number of collisions is 5.
    # The cars start out being very far from each other.
    # After one time step, they are closer together.
    # After two time steps, they are very close together.
    # After three time steps, they are side by side.
    # After four time steps, they are almost touching.
    # After five time steps, they are touching each other.
    # Therefore, the number of collisions is 5.
    # If n = 50, the number of collisions is 50.
    # If n = 100, the number of collisions is 100.
    # The number of collisions grows linearly with n.

    # This function returns the number of collisions.
    return n
