def check_scenario(scenario: str, liar_count: set, statements: dict, days_of_week: set) -> bool:
    """
    Evaluates the consistency of a scenario where one participant is the criminal based on the given statements.

    This function takes a potential criminal's name (scenario) and a set of liars (liar_count) and checks if
    the statements made by all participants are consistent with this scenario, disregarding any statements
    about the day of the week.

    Parameters:
    - scenario (str): The name of the participant being tested as the potential criminal.
    - liar_count (set): A set of names of participants who are assumed to be liars.
    - statements (dict): A dictionary mapping participant names to lists of their respective statements.
    - days_of_week (set): A set of strings representing the days of the week.

    Returns:
    - bool: True if the scenario is consistent with the statements, False otherwise.

    Test Cases:
    >>> check_scenario("ALICE", {"BOB", "CHARLIE"}, {"ALICE": ["I am guilty."], "BOB": ["ALICE is not guilty."], "CHARLIE": []}, {"MONDAY", "TUESDAY"})
    True
    """
    # Initialize a set to store all statements that mention the liars
    liars_statements = set()
    # Initialize a set to store all statements that mention the potential criminal
    criminal_statements = set()
    for speaker, statement in statements.items():
        if speaker in liar_count:
            liars_statements.update(statement)
        elif speaker == scenario:
            criminal_statements.update(statement)
    # Check if any liars statements contain the name of the criminal
    for statement in liars_statements:
        if scenario in statement:
            return False
    # Check if the criminal's statements contain names of the liars or any day of the week
    for statement in criminal_statements:
        if any(name in statement for name in liar_count):
            return False
        if any(day in statement for day in days_of_week):
            return False
    return True
def test_check_scenario():
    # Define a set of days of the week for the test cases
    days_of_week = set(["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"])

    # Test case 1: Simple case where the scenario is correct
    statements_test1 = {
        "ALICE": ["I am not guilty.", "BOB is guilty."],
        "BOB": ["ALICE is not guilty.", "Today is MONDAY"],
        "CHARLIE": ["I am guilty."]
    }
    scenario_test1 = "CHARLIE"
    liar_count_test1 = {"ALICE", "BOB"}
    assert check_scenario(scenario_test1, liar_count_test1, statements_test1, days_of_week) == False, "Test case 1 failed"

    # Test case 2: Scenario with contradictory statements
    statements_test2 = {
        "ALICE": ["I am guilty."],
        "BOB": ["I am not guilty.", "ALICE is guilty."],
        "CHARLIE": ["I am not guilty.", "Today is TUESDAY"]
    }
    scenario_test2 = "ALICE"
    liar_count_test2 = {"BOB", "CHARLIE"}
    assert check_scenario(scenario_test2, liar_count_test2, statements_test2, days_of_week) == False, "Test case 2 failed"

    # Test case 3: Scenario where the statements are ambiguous
    statements_test3 = {
        "ALICE": ["I am not guilty.", "Today is WEDNESDAY"],
        "BOB": ["I am not guilty.", "CHARLIE is guilty."],
        "CHARLIE": ["BOB is not guilty."]
    }
    scenario_test3 = "BOB"
    liar_count_test3 = {"ALICE", "CHARLIE"}
    assert check_scenario(scenario_test3, liar_count_test3, statements_test3, days_of_week) == False, "Test case 3 failed"

    print("All test cases passed.")

# Run the test function
test_check_scenario()