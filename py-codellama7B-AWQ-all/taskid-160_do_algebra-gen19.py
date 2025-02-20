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

    # Example:
    # operator: ['+', '*', '-']
    # operand: [2, 3, 4, 5]
    # Result: 2 + 3 * 4 - 5
    # Result: 9
    total = 0
    for index, operator_value in enumerate(operator):
        left_operand = operand[index]
        if operator_value == '+' or operator_value == '-':
            total = total + left_operand
        elif operator_value == '*':
            total = total * left_operand
        else:
            total = total // left_operand
        if index != len(operator) - 1:
            total = total + operand[index+1]
        else:
            total = total + operand[index+1]
    return total
