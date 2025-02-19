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
        raise Exception('The length of operator list must be equal to the length of operand list minus one.')
    if len(operand) < 2:
        raise Exception('Operand list must have at least two operands.')

    result = operand[0]
    for i, oper in enumerate(operator):
        operand_ = operand[i+1]
        if oper == '+':
            result += operand_
        elif oper == '-':
            result -= operand_
        elif oper == '*':
            result *= operand_
        elif oper == '//':
            result //= operand_
        elif oper == '**':
            result **= operand_
        else:
            raise Exception('Unknown operator: %s' % oper)
    return result
