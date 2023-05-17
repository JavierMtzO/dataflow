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
    semantic_cube = Semantic_Cube()
    temp_variables = {}
    temp_variables_counter = 1

    quadruple_counter = 0
    quadruples : list[Quadruple] = []

    simple_counter = 0


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
        operand_type = type(operand).__name__
        if operand_type == 'str':
            operand_type = self.variables_table.get_type(operand)
            operand = self.variables_table.get_value(operand)
        self.operands_stack.append(operand)
        self.types_stack.append(operand_type)
    
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
        operand_type = self.types_stack.pop()
        variable_type = self.types_stack.pop()
        operator = self.operators_stack.pop()
        left_operand = self.operands_stack.pop()
        result = self.operands_stack.pop()
        self.semantic_cube.match_types(variable_type, operand_type, operator)
        quadruple = Quadruple(operation=operator, left_operand=left_operand, result=result)
        self.variables_table.change_variable_value(result, left_operand)
        self.append_quad(quadruple)
    
    def aritmetics_operation(self) -> None:
        # Get operands, types and operator
        right_operand = self.operands_stack.pop()
        right_operand_type = self.types_stack.pop()
        left_operand = self.operands_stack.pop()
        left_operand_type = self.types_stack.pop()
        operator = self.operators_stack.pop()
        # Generate new temporal variable
        temporal_variable = f"t{self.temp_variables_counter}"
        temp_var_type = self.semantic_cube.match_types(left_operand_type, right_operand_type, operator)
        expression = f"{left_operand} {operator} {right_operand}"
        self.temp_variables[temporal_variable] = eval(expression)
        self.temp_variables_counter += 1
        # Append temporal variable to operand stack and type stack
        self.operands_stack.append(self.temp_variables[temporal_variable])
        self.types_stack.append(temp_var_type)
        # Generate quadruple
        quadruple = Quadruple(operation=operator, left_operand=left_operand, right_operand = right_operand ,result=temporal_variable)
        self.append_quad(quadruple)

    def print_quad(self) -> None:
        operand = self.operands_stack.pop()
        operator = self.operators_stack.pop()
        self.types_stack.pop()
        print(operand)
        quadruple = Quadruple(operation=operator,result=operand)
        self.append_quad(quadruple)



