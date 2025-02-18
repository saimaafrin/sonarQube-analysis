def is_equal_to_sum_even(n: int) -> bool:
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    >>> is_equal_to_sum_even(4)
    False
    >>> is_equal_to_sum_even(6)
    False
    >>> is_equal_to_sum_even(8)
    True
    """

    # Check if the given number is even
    if n % 2 != 0:
        return False

    # Initialize a list to hold the four even numbers
    numbers_list = []

    # Initialize a variable to hold the number of even numbers
    number_of_even_numbers = 0

    # Initialize a variable to hold the sum of the even numbers
    sum_of_even_numbers = 0

    # Loop through the range of numbers from 1 to the given number
    for number in range(1, n + 1):

        # If the number is even
        if number % 2 == 0:

            # Add the number to the list of even numbers
            numbers_list.append(number)

            # Increment the number of even numbers
            number_of_even_numbers += 1

            # Calculate the sum of the even numbers
            sum_of_even_numbers = sum(numbers_list)

            # Check if the sum of the even numbers is equal to the given number
            if sum_of_even_numbers == n:

                # Return True
                return True

    # Return False if the given number is not equal to the sum of 4 even numbers
    return False
