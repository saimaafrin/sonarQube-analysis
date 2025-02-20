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

    if len(operator) == 0 or len(operand) == 0:
        raise ValueError('list length is zero!')

    if len(operator) != len(operand) - 1:
        raise ValueError('list length is not match!')

    for op in operand:
        if op < 0:
            raise ValueError('operand list contains a negative number!')

    def build_expression(operator: List[str], operand: List[int]) -> int:
        """
        Build the algebric expression
        """
        if len(operator) == 0:
            raise ValueError('list length is zero!')

        expression = f"{operand[0]}"

        for i in range(1, len(operator)):
            expression = f"{expression} {operator[i-1]} {operand[i]}"

        return eval(expression)

    return build_expression(operator, operand)
