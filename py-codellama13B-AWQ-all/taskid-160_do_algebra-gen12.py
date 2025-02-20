from typing import List

def do_algebra(operator: List[str], operand: List[int]) -> int:
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """

    # Initialize variables
    current_operand = 0
    result = 0
    operator_length = len(operator)

    # Iterate through the lists
    while current_operand < operator_length:
        # Get the current operand
        current_operand = current_operand + 1
        # Check if there is a next operator
        if current_operand < operator_length:
            # Get the next operator
            current_operator = operator[current_operand]

            # Perform the operation
            if current_operator == '+':
                result = result + operand[current_operand]
            elif current_operator == '-':
                result = result - operand[current_operand]
            elif current_operator == '*':
                result = result * operand[current_operand]
            elif current_operator == '//':
                result = result // operand[current_operand]
            elif current_operator == '**':
                result = result ** operand[current_operand]

    return result
