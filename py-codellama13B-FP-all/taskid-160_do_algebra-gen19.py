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

    if len(operator) != len(operand) - 1:
        raise ValueError('length of operator list must be equal to length of operand list minus one')
    if len(operand) < 2:
        raise ValueError('operand list must have at least two operands')
    if len(operator) < 1:
        raise ValueError('operator list must have at least one operator')
    if not all(isinstance(i, int) for i in operand) or not all(isinstance(i, str) for i in operator):
        raise ValueError('operand and operator lists must be lists of integers and strings')
    if not all(i >= 0 for i in operand):
        raise ValueError('operand list must be non-negative integers')

    eval_str = f"{operand[0]}{operator[0]}{operand[1]}"
    for i in range(2, len(operand)):
        eval_str += f"{operator[i-1]}{operand[i]}"
    result = eval(eval_str)
    return result
