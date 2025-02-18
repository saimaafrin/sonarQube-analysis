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

    # base case
    if len(operator) == 0:
        return operand[0]

    # recursive case
    # get the first element of operand and the first element of operator
    result = do_algebra(operator[1:], operand[1:])
    # perform operation using the first element of operand and the first element of operator
    if operator[0] == '+':
        result += operand[0]
    elif operator[0] == '-':
        result -= operand[0]
    elif operator[0] == '*':
        result *= operand[0]
    elif operator[0] == '//':
        result //= operand[0]
    elif operator[0] == '**':
        result **= operand[0]
    return result
