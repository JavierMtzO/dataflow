import ast
from collections import deque
import numpy as np

from Memories.virtual_memory import VirtualMemory
from Semantics.quadruple import Quadruple
from Semantics.semantic_cube import Semantic_Cube
from Semantics.variables_table import Functions_Directory, Variables_Table


class Semantics:
    operands_stack = deque()
    operators_stack = deque()
    types_stack = deque()
    jumps_stack = deque()
    id_queue = deque()
    functions_directory = Functions_Directory()
    semantic_cube = Semantic_Cube()
    temp_variables = {}
    temp_variables_counter = 1
    quadruple_counter = 0
    quadruples : list[Quadruple] = []
    for_vc_stack = deque()
    for_vf_stack = deque()
    temp_for_counter = 1
    current_scope = "global"
    parameters_list = []

    global_variables_table = Variables_Table()
    local_variables_table = Variables_Table()

    final_global_mem = ""
    final_global_constant_dict = {}

    virtual_memory = VirtualMemory()


    def add_id(self, id: str) -> None:
        self.id_queue.append(id)
    
    def add_type(self, type: str, current: bool) -> None:
        if current:
            self.current_type = type
            self.types_stack.append(type)
        else:
            self.types_stack.append(type)
    
    def add_function_type(self) -> None:
        function_type = self.types_stack.pop()
        self.types_stack.append(function_type)
        self.types_stack.append(function_type)
    
    def add_operator(self, operator:str) -> None:
        self.operators_stack.append(operator)
    
    def add_operand(self, operand) -> None:
        operand_type = type(operand).__name__
        if operand_type == 'str':
            if self.global_variables_table.lookup_variable(operand):
                operand_type = self.global_variables_table.get_type(operand)
                if self.local_variables_table.lookup_variable(operand):
                    operand_type = self.local_variables_table.get_type(operand)
            elif self.local_variables_table.lookup_variable(operand):
                    operand_type = self.local_variables_table.get_type(operand)
            else:
                raise Exception(f'Variable "{operand}" has not been declared!')
        else:
            operand = str(operand)
            virtual_direction = self.virtual_memory.assign_virtual_address(type=operand_type, is_const=True)
            if self.current_scope == "global":
                if not self.global_variables_table.lookup_variable(operand):
                    self.global_variables_table.push_variable(name=operand, type=operand_type, kind='const', virtual_direction=virtual_direction)
            elif self.current_scope == "local":
                if not self.local_variables_table.lookup_variable(operand):
                    self.local_variables_table.push_variable(name=operand, type=operand_type, kind='const', virtual_direction=virtual_direction)
        self.operands_stack.append(operand)
        self.types_stack.append(operand_type)
    
    def save_ids(self, is_parameter:bool=False) -> None:
        while len(self.id_queue) > 0:
            name = self.id_queue.pop()
            type = self.types_stack.pop()
            if self.current_scope == "local":
                virtual_direction = self.virtual_memory.assign_virtual_address(type=type, is_global=False)
                self.local_variables_table.push_variable(name= name, type= type, kind='var', virtual_direction=virtual_direction)
                if is_parameter:
                    self.parameters_list.append(type)
            elif self.current_scope == "global":
                virtual_direction = self.virtual_memory.assign_virtual_address(type=type, is_global=True)
                self.global_variables_table.push_variable(name= name, type= type, kind='var', virtual_direction=virtual_direction)
    
    def save_function(self) -> None:
        name = self.id_queue.pop()
        type = self.types_stack.pop()
        if type == 'program':
            self.functions_directory.push_function(name=name, type=type)
        elif self.current_scope != "local":
            self.functions_directory.push_function(name=name, type=type, dir=self.quadruple_counter)
            self.current_scope = "local"
            self.operands_stack.append(name)
            self.types_stack.append(type)
    
    def return_quad(self) -> None:
        expressions_type = self.types_stack.pop()
        function_type = self.types_stack.pop()
        operator = 'return'
        operand = self.operands_stack.pop()
        name = self.functions_directory.get_current_function()
        if expressions_type != function_type:
            raise Exception(f'Function "{name}" is declared as a {function_type} and it is returning {expressions_type}')
        operand_virtual_direction = self.local_variables_table.get_virtual_memory(name=operand)
        if operand_virtual_direction == -1:   
            operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=operand)
        quadruple = Quadruple(operation=operator, result=operand_virtual_direction)
        self.append_quad(quadruple)
    
    def save_function_as_variable(self) -> None:
        expressions_type = self.types_stack.pop()
        function_type = self.types_stack.pop()
        operand = self.operands_stack.pop()
        name = self.functions_directory.get_current_function()
        if expressions_type != function_type:
            raise Exception(f'Function "{name}" is declared as a {function_type} and it is returning {expressions_type}')
        if not self.global_variables_table.lookup_variable(operand):
            virtual_direction = self.virtual_memory.assign_virtual_address(type=function_type, is_global=True)
            self.global_variables_table.push_variable(name=name, type=expressions_type, kind='var', virtual_direction=virtual_direction)
        if not self.local_variables_table.lookup_variable(operand):
            virtual_direction = self.virtual_memory.assign_virtual_address(type=function_type, is_global=False)
            self.local_variables_table.push_variable(name=name, type=expressions_type, kind='var', virtual_direction=virtual_direction)
        self.types_stack.append(function_type)

    
    def add_parameters(self) -> None:
        currenct_function = self.functions_directory.get_current_function()
        self.functions_directory.push_parameters(name=currenct_function, parameters_list=str(self.parameters_list))
    
    def get_variable(self, name: str) -> None:
        if self.global_variables_table.lookup_variable(name):
            self.types_stack.append(self.global_variables_table.get_type(name))
        elif self.local_variables_table.lookup_variable(name):
            self.types_stack.append(self.local_variables_table.get_type(name))
        else: 
            raise Exception(f'{name} is not declared')
        self.operands_stack.append(name)

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
        if self.current_scope == "global":
            result_virtual_direction = self.global_variables_table.get_virtual_memory(name=result)
            left_operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=left_operand)
        elif self.current_scope == "local":
            result_virtual_direction = self.local_variables_table.get_virtual_memory(name=result)
            left_operand_virtual_direction = self.local_variables_table.get_virtual_memory(name=left_operand)
            if result_virtual_direction == -1:
                result_virtual_direction = self.global_variables_table.get_virtual_memory(name=result)
            if left_operand_virtual_direction == -1:
                left_operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=left_operand)   
        quadruple = Quadruple(operation=operator, left_operand=left_operand_virtual_direction, result=result_virtual_direction)
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
        self.temp_variables[temporal_variable] = temporal_variable
        virtual_direction = self.virtual_memory.assign_virtual_address(type=temp_var_type, is_temp=True)
        if self.current_scope == "local":
            self.local_variables_table.push_variable(name=temporal_variable, type=temp_var_type, kind='temp', virtual_direction=virtual_direction)
            left_operand_virtual_direction = self.local_variables_table.get_virtual_memory(name=left_operand)
            if left_operand_virtual_direction == -1:
                left_operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=left_operand)
            right_operand_virtual_direction = self.local_variables_table.get_virtual_memory(name=right_operand)
            if right_operand_virtual_direction == -1:
                right_operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=right_operand) 
        if self.current_scope == "global":
            self.global_variables_table.push_variable(name=temporal_variable, type=temp_var_type, kind='temp', virtual_direction=virtual_direction)
            left_operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=left_operand)
            right_operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=right_operand)
        self.temp_variables_counter += 1
        # Append temporal variable to operand stack and type stack
        self.operands_stack.append(self.temp_variables[temporal_variable])
        self.types_stack.append(temp_var_type)
        # Generate quadruple
        
        quadruple = Quadruple(operation=operator, left_operand=left_operand_virtual_direction, right_operand = right_operand_virtual_direction ,result=virtual_direction)
        self.append_quad(quadruple)

    def print_quad(self) -> None:
        operand = self.operands_stack.pop()
        operator = self.operators_stack.pop()
        self.types_stack.pop()
        if self.current_scope == "global":
            operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=operand)
        elif self.current_scope == "local":
            operand_virtual_direction = self.local_variables_table.get_virtual_memory(name=operand)
            if operand_virtual_direction == -1:
                operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=operand)
        quadruple = Quadruple(operation=operator,result=operand_virtual_direction)
        self.append_quad(quadruple)

    def go_to_false_quad(self) -> None:
        operand = self.operands_stack.pop()
        if self.current_scope == "global":
            operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=operand)
        elif self.current_scope == "local":
            operand_virtual_direction = self.local_variables_table.get_virtual_memory(name=operand)
            if operand_virtual_direction == -1:
                operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=operand)
        self.jumps_stack.append(self.quadruple_counter)
        quadruple = Quadruple(operation="gotof", left_operand=operand_virtual_direction)
        self.append_quad(quadruple)
        self.operands_stack.append(operand)
    
    def go_to_true_quad(self) -> None:
        operand = self.operands_stack.pop()
        if self.current_scope == "global":
            operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=operand)
        elif self.current_scope == "local":
            operand_virtual_direction = self.local_variables_table.get_virtual_memory(name=operand)
            if operand_virtual_direction == -1:
                operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=operand)
        self.jumps_stack.append(self.quadruple_counter)
        quadruple = Quadruple(operation="gotot", left_operand=operand_virtual_direction)
        self.append_quad(quadruple)
    
    def go_to_quad(self) -> None:
        result = self.jumps_stack.pop()
        quadruple = Quadruple(operation="goto", result=result)
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
    
    def fill_go_to_true_quad(self, jumps:int=0) -> None:
        index = self.jumps_stack.pop()
        self.quadruples[index].result = self.quadruple_counter + jumps
    
    def check_exact_type_for(self, type: str=None) -> None:
        exp_type = self.types_stack.pop()
        if not exp_type == type:
            raise Exception(f'Value must be {type}')
        self.types_stack.append(exp_type)
        
    
    def add_final_counter_for(self) -> None:
        self.for_vf_stack.append(self.operands_stack.pop())
    
    def check_boolean_expression_for(self) -> tuple[str,str,str]:
        vf = self.for_vf_stack.pop()
        vc = self.for_vc_stack.pop()
        operator = '<='
        self.for_vf_stack.append(vf)
        self.for_vc_stack.append(vc)
        return vc,vf,operator
    
    def generate_for_quad(self) -> None:
        vc,vf,operator = self.check_boolean_expression_for()
        right_type = self.types_stack.pop()
        left_type = self.types_stack.pop()
        
        # Generate new temporal variable
        temp_var_type = self.semantic_cube.match_types(left_type, right_type, operator)
        temporal_variable = f"vf{self.temp_for_counter}"
        self.temp_for_counter += 1
        temp_virtual_direction = self.virtual_memory.assign_virtual_address(type=temp_var_type, is_temp=True)
        if self.current_scope == "local":
            self.local_variables_table.push_variable(name=temporal_variable, type=temp_var_type, kind='temp', virtual_direction=temp_virtual_direction)
            vc_virtual_direction = self.local_variables_table.get_virtual_memory(name=vc)
            vf_virtual_direction = self.local_variables_table.get_virtual_memory(name=vf)
        if self.current_scope == "global":
            self.global_variables_table.push_variable(name=temporal_variable, type=temp_var_type, kind='temp', virtual_direction=temp_virtual_direction)
            vc_virtual_direction = self.global_variables_table.get_virtual_memory(name=vc)
            vf_virtual_direction = self.global_variables_table.get_virtual_memory(name=vf)
        quadruple = Quadruple(operation=operator, left_operand=vc_virtual_direction, right_operand = vf_virtual_direction ,result=temp_virtual_direction)
        self.append_quad(quadruple)
        self.jumps_stack.append(self.quadruple_counter - 1)
        self.operands_stack.append(temporal_variable)
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
    
    def end_function(self) -> None:
        self.parameters_list = []
        types_array = self.local_variables_table.get_types_counter_list(is_local=True)
        current_function = self.functions_directory.get_current_function()
        self.functions_directory.push_variables_types_used(name=current_function, types_array=types_array)
        quadruple = Quadruple(operation='endfunc')
        self.append_quad(quadruple)
        self.virtual_memory.restart_local_memory()
    
    def empty_variables_table(self, is_local: bool = False) -> None:
        if is_local:
            print(f"Local Variables Table for function {self.functions_directory.get_current_function()}: ")
            self.end_function()
            self.local_variables_table.print_variables_table()
            self.final_global_constant_dict.update(self.local_variables_table.get_constant_dict())
            self.local_variables_table.empty_variables_table()
            self.current_scope = "global"
        else:
            self.final_global_mem = self.global_variables_table.get_types_counter_list()
            self.final_global_constant_dict.update(self.global_variables_table.get_constant_dict())
            print("Functions Directory: ")
            self.functions_directory.print_functions_directory()
            print("Global Variables Table: ")
            self.global_variables_table.print_variables_table()
            self.global_variables_table.empty_variables_table()
            self.end_program()
    
    def era_quad(self, current_function:str) -> None:
        self.current_function = current_function
        if self.functions_directory.lookup_function(name=current_function):
            resources = self.functions_directory.get_variables_types_used(current_function)
            if not isinstance(resources, str):
                if np.isnan(resources):
                    types_array = self.local_variables_table.get_types_counter_list(is_local=True)
                    self.functions_directory.push_variables_types_used(name=current_function, types_array=types_array)
                    resources = self.functions_directory.get_variables_types_used(current_function)
            quadruple = Quadruple(operation='era', result=resources)
            self.append_quad(quadruple)
            # Get parameters string, convert it to list and finally to a deque
            self.parameters_stack = deque(ast.literal_eval(self.functions_directory.get_parameters(current_function)))
            self.function_dir = self.functions_directory.get_dir(current_function)
        else:
            raise Exception(f'Function "{current_function}" has not been declared!')
    
    def param_quad(self) -> None:
        original_parameter_type = self.parameters_stack.popleft()
        current_parameter_type = self.types_stack.pop()
        operand = self.operands_stack.pop()
        if original_parameter_type != current_parameter_type:
            raise Exception(f'Tried to call a parameter of type "{current_parameter_type}" when a parameter of {original_parameter_type} is required')
        if self.current_scope == "global":
            operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=operand)
        elif self.current_scope == "local":
            operand_virtual_direction = self.local_variables_table.get_virtual_memory(name=operand)
            if operand_virtual_direction == -1:
                operand_virtual_direction = self.global_variables_table.get_virtual_memory(name=operand)
        parameter_virtual_direction = self.virtual_memory.assign_virtual_address_parameter(type=current_parameter_type)
        quadruple = Quadruple(operation='param', left_operand=operand_virtual_direction, result=parameter_virtual_direction)
        self.append_quad(quadruple)
    
    def go_sub_quad(self) -> None:
        self.virtual_memory.restart_parameters()
        quadruple = Quadruple(operation='gosub', result=self.function_dir)
        self.append_quad(quadruple)
        if self.current_scope == "local":
            temp_var_type = self.local_variables_table.get_type(name=self.current_function)
            function_virtual_direction = self.local_variables_table.get_virtual_memory(name=self.current_function)
        if self.current_scope == "global":
            temp_var_type = self.global_variables_table.get_type(name=self.current_function)
            function_virtual_direction = self.global_variables_table.get_virtual_memory(name=self.current_function)
        temporal_variable = f"t{self.temp_variables_counter}"
        self.temp_variables_counter += 1
        operator = '='
        temp_virtual_direction = self.virtual_memory.assign_virtual_address(type=temp_var_type, is_temp=True)
        if self.current_scope == "local":
            self.local_variables_table.push_variable(name=temporal_variable, type=temp_var_type, kind='temp', virtual_direction=temp_virtual_direction)
        if self.current_scope == "global":
            self.global_variables_table.push_variable(name=temporal_variable, type=temp_var_type, kind='temp', virtual_direction=temp_virtual_direction)
        quadruple = Quadruple(operation=operator, left_operand=function_virtual_direction, result=temp_virtual_direction)
        self.append_quad(quadruple)
        self.operands_stack.append(temporal_variable)
        self.types_stack.append(temp_var_type)
    
    def functions_assignation(self) -> None:
        variable = self.operands_stack.pop()
        variable_type = self.types_stack.pop()
        function_name = self.functions_directory.get_name(self.current_function)
        function_type = self.functions_directory.get_type(self.current_function)
        if variable_type != function_type:
            raise Exception(f'Cannot assign "{variable_type}" to function of type {function_type}')
        self.operands_stack.append(variable)
        self.operands_stack.append(function_name)
        self.types_stack.append(variable_type)
        self.types_stack.append(function_type)
    
    def end_program(self) -> None:
        quadruple = Quadruple(operation='endprogram')
        self.append_quad(quadruple)







