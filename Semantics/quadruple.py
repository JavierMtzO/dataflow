from Semantics.semantic_cube import operations

quadruple_operations = operations | {
    'goto': 50,
    'gotot': 51,
    'gotof': 52,
}

class Quadruple:
    
    def __init__(self, operation: str, left_operand: int, result: int, right_operand: int = None) -> None:
        if operation not in quadruple_operations:
            raise Exception('Unkown operation on quadruple')
        self.op_code = quadruple_operations[operation]
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result
    
    def print_quadruple(self) -> str:
        return f'{self.op_code} {self.left_operand} {self.right_operand} {self.result}'