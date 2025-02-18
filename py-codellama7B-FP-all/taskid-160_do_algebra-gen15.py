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

    # implement your logic here
    if operator == [] or operand == []:
        return -1
    if len(operator) == 1 and len(operand) == 1:
        return operand[0]
    if len(operand) == 1 and len(operator) > 1:
        return -1
    if len(operand) > 1 and len(operator) == 1:
        return operand[0]
    if len(operand) == 0 or len(operator) == 0:
        return -1
    if len(operand) != len(operator):
        return -1
    if len(operand) - 1 != len(operator):
        return -1
    if len(operand) > 1 and len(operator) == 1:
        return -1
    if len(operand) == 0 or len(operator) == 0:
        return -1
    result = 0
    for i in range(len(operator)):
        if operator[i] == '+':
            result = operand[i] + result
        elif operator[i] == '-':
            result = operand[i] - result
        elif operator[i] == '*':
            result = operand[i] * result
        elif operator[i] == '//':
            result = operand[i] // result
        elif operator[i] == '**':
            result = operand[i] ** result
    return result
