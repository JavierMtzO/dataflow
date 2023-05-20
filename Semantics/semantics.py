from collections import deque
from Semantics.variables_table import Variables_Table, Functions_Directory
from Semantics.quadruple import Quadruple
from Semantics.semantic_cube import Semantic_Cube

class Semantics:
    operands_stack = deque()
    operators_stack = deque()
    types_stack = deque()
    jumps_stack = deque()
    id_queue = deque()
    global_variables_table = Variables_Table()
    functions_directory = Functions_Directory()
    semantic_cube = Semantic_Cube()
    temp_variables = {}
    temp_variables_counter = 1
    quadruple_counter = 0
    quadruples : list[Quadruple] = []
    for_vc_stack = deque()
    for_vf_stack = deque()
    temp_for_counter = 1


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
            operand_type = self.global_variables_table.get_type(operand)
            operand = self.global_variables_table.get_value(operand)
        self.operands_stack.append(operand)
        self.types_stack.append(operand_type)
    
    def save_ids(self) -> None:
        while len(self.id_queue) > 0:
            name = self.id_queue.pop()
            type = self.types_stack.pop()
            self.global_variables_table.push_variable(name= name, type= type)
    
    def save_function(self) -> None:
        name = self.id_queue.pop()
        type = self.types_stack.pop()
        self.functions_directory.push_function(name=name, type=type)
    
    def get_variable(self, name: str) -> None:
        if not self.global_variables_table.lookup_variable(name):
            raise Exception(f'{name} is not declared')
        self.operands_stack.append(name)
        self.types_stack.append(self.global_variables_table.get_type(name))

    def append_quad(self, quadruple: Quadruple) -> None:
        self.quadruples.append(quadruple)
        self.quadruple_counter += 1

    def assignment_quad(self, is_for: bool=False) -> None:
        operand_type = self.types_stack.pop()
        variable_type = self.types_stack.pop()
        operator = self.operators_stack.pop()
        left_operand = self.operands_stack.pop()
        result = self.operands_stack.pop()
        result_type = self.semantic_cube.match_types(variable_type, operand_type, operator)
        quadruple = Quadruple(operation=operator, left_operand=left_operand, result=result)
        self.global_variables_table.change_variable_value(result, left_operand)
        self.append_quad(quadruple)
        if is_for:
            self.for_vc_stack.append(result)
            self.types_stack.append(result_type)
    
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
        # TESTING #
        # expression = f"{left_operand} {operator} {right_operand}"
        # self.temp_variables[temporal_variable] = eval(expression)
        ###########
        self.temp_variables[temporal_variable] = temporal_variable

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
        quadruple = Quadruple(operation=operator,result=operand)
        self.append_quad(quadruple)

    def go_to_false_quad(self) -> None:
        self.jumps_stack.append(self.quadruple_counter)
        quadruple = Quadruple(operation="gotof")
        self.append_quad(quadruple)
    
    def fill_go_to_false_quad(self,  jumps:int=1) -> None:
        index = self.jumps_stack.pop()
        self.quadruples[index].result = self.quadruple_counter + jumps
    
    def go_to_main(self) -> None:
        self.jumps_stack.append(self.quadruple_counter)
        quadruple = Quadruple(operation="goto")
        self.append_quad(quadruple)

    def fill_go_to_main_quad(self,  jumps:int=1) -> None:
        index = self.jumps_stack.pop()
        self.quadruples[index].result = self.quadruple_counter

    def fill_go_to_false_quad(self,  jumps:int=1) -> None:
        index = self.jumps_stack.pop()
        self.quadruples[index].result = self.quadruple_counter + jumps
    
    def go_to_true_quad(self) -> None:
        self.jumps_stack.append(self.quadruple_counter)
        quadruple = Quadruple(operation="gotot")
        self.append_quad(quadruple)
    
    def go_to_quad(self) -> None:
        result = self.jumps_stack.pop()
        quadruple = Quadruple(operation="goto", result=result)
        self.append_quad(quadruple)
    
    def fill_go_to_true_quad(self, jumps:int=0) -> None:
        index = self.jumps_stack.pop()
        self.quadruples[index].result = self.quadruple_counter + jumps
    
    def check_exact_type_for(self, type: str=None) -> None:
        exp_type = self.types_stack.pop()
        if not exp_type == type:
            raise Exception(f'Value must be {type}')
    
    def add_final_counter_for(self) -> None:
        self.for_vf_stack.append(self.operands_stack.pop())
    
    def check_boolean_expression_for(self) -> tuple[str,str,str]:
        vf = self.for_vf_stack.pop()
        vc_var = self.for_vc_stack.pop()
        vc = self.global_variables_table.get_value(vc_var)
        operator = '<'
        self.for_vf_stack.append(vf)
        self.for_vc_stack.append(vc_var)
        return vc,vf,operator
    
    def generate_for_quad(self) -> None:
        vc,vf,operator = self.check_boolean_expression_for()
        # Generate new temporal variable
        temporal_variable = f"vf{self.temp_for_counter}"
        expression = f"{vc} {operator} {vf}"
        self.temp_variables[temporal_variable] = eval(expression)
        self.temp_for_counter += 1
        quadruple = Quadruple(operation=operator, left_operand=vc, right_operand = vf ,result=temporal_variable)
        self.append_quad(quadruple)
        self.jumps_stack.append(self.quadruple_counter - 1)
        self.go_to_false_quad()
    
    def end_for(self) -> None:
        self.for_vf_stack.pop()
        self.for_vc_stack.pop()
        self.fill_go_to_false_quad()
        self.go_to_quad()
    
    def pop_operand(self) -> None:
        self.operands_stack.pop()
    def pop_type(self) -> None:
        self.types_stack.pop()
    def append_jump(self) -> None:
        self.jumps_stack.append(self.quadruple_counter)
    
    def print_aux(self, text:str) -> None:
        print(text)



