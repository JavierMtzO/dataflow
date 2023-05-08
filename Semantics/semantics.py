from collections import deque
from Semantics.variables_table import Variables_Table
from Semantics.quadruple import Quadruple

class Semantics:
    operands_stack = deque()
    operators_stack = deque()
    types_stack = deque()
    jumps_stack = deque()
    id_queue = deque()
    variables_table = Variables_Table()

    quadruple_counter = 0
    quadruples : list[Quadruple] = []


    def add_id(self, id: str) -> None:
        self.id_queue.append(id)
    
    def add_type(self, type: str) -> None:
        self.types_stack.append(type)
    
    def save_id(self) -> None:
        name = self.id_queue.popleft()
        type = self.types_stack.pop()
        self.variables_table.push_variable(name= name, type= type)
    
    def append_quad(self, quadruple: Quadruple) -> None:
        self.quadruples.append(quadruple)
        self.quadruple_counter += 1

    def assignment_quad(self) -> None:
        operator = self.operators_stack.pop()
        left_operand = self.operands_stack.pop()
        result = self.operands_stack.pop()
        quadruple = Quadruple(operation=operator, left_operand=left_operand, result=result)
        self.append_quad(quadruple)
