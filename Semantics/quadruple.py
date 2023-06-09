from Semantics.semantic_cube import operations

quadruple_operations = operations | {
    'goto' : 'goto',
    'gotot': 'gotot',
    'gotof': 'gotof',
    'print': 'print',
    'endfunc':'endfunc',
    'era': 'era',
    'gosub': 'gosub',
    'param': 'param',
    'return': 'return',
    'endprogram':'endprogram',
    'ver':'ver',
    'base_sum':'base_sum'

}

class Quadruple:
    """
    Class: Quadruple
    
    Represents a quadruple in a dataflow language.

    Attributes:
        op_code (str): The operation code of the quadruple.
        left_operand (int): The left operand of the quadruple.
        right_operand (int): The right operand of the quadruple.
        result (int): The result of the quadruple.

    Methods:
        print_quadruple(): Prints the quadruple in a readable format.
    """
    
    def __init__(self, operation: str, left_operand: int = None, right_operand: int = None, result: int = None) -> None:
        if operation not in quadruple_operations:
            raise Exception('Unkown operation on quadruple')
        self.op_code = quadruple_operations[operation]
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result
    
    def print_quadruple(self) -> str:
        return f'{self.op_code} {self.left_operand} {self.right_operand} {self.result}'