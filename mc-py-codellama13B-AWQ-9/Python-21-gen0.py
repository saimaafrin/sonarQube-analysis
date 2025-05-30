from typing import List, Tuple
def select_volunteers(n: int, m: int, applicants: List[Tuple[int, int]]) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Selects and determines the interview score cutoff and the list of applicants who qualify for the interview process.
    
    The function sorts the applicants based on their test scores in descending order. If multiple applicants have the same score,
    they are then sorted by their registration number in ascending order. The interview score cutoff is calculated based on 150%
    of the planned number of recruits, rounded down. All applicants with scores equal to or higher than the cutoff are considered
    qualified for the interview.
    
    Args:
    - n (int): The total number of applicants.
    - m (int): The planned number of volunteers to be recruited.
    - applicants (List[Tuple[int, int]]): A list of tuples where each tuple contains the registration number and test score of an applicant.
    
    Returns:
    - Tuple[int, List[Tuple[int, int]]]: A tuple containing the interview score cutoff and a list of tuples, each of which includes
      the registration number and test score of qualified applicants.
    
    Examples:
    >>> select_volunteers(6, 3, [(1000, 90), (3239, 88), (2390, 95), (7231, 84), (1005, 95), (1001, 88)])
    (88, [(1005, 95), (2390, 95), (1000, 90), (1001, 88), (3239, 88)])
    """
    cutoff = 150 * m // 100
    applicants.sort(key = lambda x: (-x[1], x[0]))
    qualified = [(applicants[i][0], applicants[i][1]) for i in range(n) if applicants[i][1] >= cutoff]
    return (cutoff, qualified)
def test_select_volunteers():
    # Define test cases
    test_cases = [
        (6, 3, [(1000, 90), (3239, 88), (2390, 95), (7231, 84), (1005, 95), (1001, 88)],
         (88, [(1005, 95), (2390, 95), (1000, 90), (1001, 88), (3239, 88)])),
        (5, 3, [(2000, 70), (2001, 80), (2002, 90), (2003, 85), (2004, 90)],
         (80, [(2002, 90), (2004, 90), (2003, 85), (2001, 80)])),
        (8, 4, [(1234, 60), (2345, 75), (3456, 85), (4567, 85), (5678, 90), (6789, 100), (7890, 65), (8901, 70)],
         (70, [(6789, 100), (5678, 90), (3456, 85), (4567, 85), (2345, 75), (8901, 70)])),
    ]

    # Run test cases
    for i, (n, m, applicants, expected) in enumerate(test_cases):
        interview_line_score, final_applicants = select_volunteers(n, m, applicants)
        assert (interview_line_score, final_applicants) == expected, f"Test case {i + 1} failed"
        print(f"Test case {i + 1} passed")

# Run the test function
test_select_volunteers()