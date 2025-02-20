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

    # Validate the operator and operand lists
    assert len(operator) == len(operand) - 1, \
        "Length of operator list must be one less than the length of operand list"

    assert len(operand) > 1, \
        "Length of operand list must be greater than 1"

    assert all(type(x) is str for x in operator), \
        "All elements of operator list must be strings"

    assert all(type(x) is int for x in operand), \
        "All elements of operand list must be integers"

    # First operand is the first element in the operand list
    result = operand[0]

    # Iterate through the operator list and perform the operations
    for idx, op in enumerate(operator):
        if op == '+':
            result += operand[idx + 1]
        elif op == '-':
            result -= operand[idx + 1]
        elif op == '*':
            result *= operand[idx + 1]
        elif op == '//':
            result //= operand[idx + 1]
        elif op == '**':
            result **= operand[idx + 1]
        else:
            raise ValueError("Invalid operator")

    return result
