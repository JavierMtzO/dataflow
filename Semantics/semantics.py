from collections import deque
from Semantics.variables_table import Variables_Table
from Semantics.quadruple import Quadruple
from Semantics.semantic_cube import Semantic_Cube

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
    
    def add_type(self, type: str, current: bool) -> None:
        if current:
            self.current_type = type
            self.types_stack.append(type)
        else:
            self.types_stack.append(type)
    
    def add_operator(self, operator:str) -> None:
        self.operators_stack.append(operator)
    
    def add_operand(self, operand) -> None:
        self.operands_stack.append(operand)
    
    def save_ids(self) -> None:
        while len(self.id_queue) > 0:
            name = self.id_queue.pop()
            type = self.types_stack.pop()
            self.variables_table.push_variable(name= name, type= type)
    
    def get_variable(self, name: str) -> None:
        if not self.variables_table.lookup_variable(name):
            raise Exception(f'{name} is not declared')
        self.operands_stack.append(name)
        self.types_stack.append(self.variables_table.get_type(name))

    def append_quad(self, quadruple: Quadruple) -> None:
        self.quadruples.append(quadruple)
        self.quadruple_counter += 1

    def assignment_quad(self) -> None:
        operator = self.operators_stack.pop()
        left_operand = self.operands_stack.pop()
        result = self.operands_stack.pop()
        quadruple = Quadruple(operation=operator, left_operand=left_operand, result=result)
        self.append_quad(quadruple)