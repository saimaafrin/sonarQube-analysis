from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """


    # sort the list in place
    l.sort()

    # now we can iterate through the list and try to find three elements
    # that sum to zero. this is more efficient than using nested loops.

    for i in range(len(l) - 2):

        # we don't need to check the same number multiple times, so we
        # skip any duplicates.

        if l[i] != l[i-1]:

            # we know that l[i] is not zero, so we can skip it.
            # it's faster than trying to divide by zero, which is an
            # error in Python.

            if l[i] != 0:

                # now we're trying to find two other numbers that sum to
                # -l[i].

                # we know that the first two elements of the triple can't
                # be the same number, so we can skip them.

                for j in range(i+1, len(l) - 1):

                    # skip duplicates
                    if l[j] != l[j-1]:

                        # now we need to find the third number.
                        # this is the fastest way to find it.

                        if -l[i] - l[j] in l[j+1:]:
                            return True

    return False
