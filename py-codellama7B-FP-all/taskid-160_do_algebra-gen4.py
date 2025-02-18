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

    assert isinstance(operator, list)
    assert isinstance(operand, list)
    assert len(operator) == len(operand) - 1
    assert all(isinstance(n, int) and n >= 0 for n in operand)
    assert len(operator) > 0
    assert len(operand) > 1

    def op(op: str, a: int, b: int) -> int:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "//":
            return a // b
        elif op == "**":
            return a ** b
        else:
            raise NotImplementedError()

    result = operand[0]
    for i in range(1, len(operand)):
        result = op(operator[i - 1], result, operand[i])
    return result
