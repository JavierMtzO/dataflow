import pandas as pd
from Semantics.semantic_cube import types, function_types

class Functions_Directory:
    def __init__(self) -> None:
        columns = ['Name', 'Type', 'Dir', 'Parameters','Variables types used']
        self.functions_directory = pd.DataFrame(columns=columns)

    def push_function(self, name: str, type: str, dir: int=None) -> None:
        if type not in function_types:
            raise Exception(f'Unknown type: "{type}"')
        if self.lookup_function(name):
            raise Exception(f'Identifier "{name}" is already declared!')
        new_function = pd.DataFrame(
            {
                'Name': name,
                'Type': type,
                'Dir': dir,
            }, index=[0])
        self.functions_directory = pd.concat([self.functions_directory, new_function], ignore_index=True)
    
    def lookup_function(self, name: str) -> bool:
        return name in self.functions_directory['Name'].values
    
    def get_type(self, name: str) -> str:
        return self.get_current_function(name).iloc[0]['Type']
    
    def get_name(self, name: str) -> str:
        return self.get_current_function(name).iloc[0]['Name']
    
    def get_variables_types_used(self, name: str) -> str:
        return self.get_current_function(name).iloc[0]['Variables types used']
    
    def get_parameters(self, name: str) -> str:
        return self.get_current_function(name).iloc[0]['Parameters']
    
    def get_dir(self, name: str) -> str:
        return self.get_current_function(name).iloc[0]['Dir']
    
    def get_current_function(self, name:str=None) -> str:
        if name is not None:
            func = self.functions_directory[self.functions_directory['Name'] == name]
            return func
        else:
            return self.functions_directory['Name'].iloc[-1]
    
    def push_variables_types_used(self, name:str ,types_array: str) -> None:
        self.functions_directory.loc[self.functions_directory['Name'] == name, 'Variables types used'] = types_array 
    
    def push_parameters(self, name:str ,parameters_list: str) -> None:
        self.functions_directory.loc[self.functions_directory['Name'] == name, 'Parameters'] = parameters_list 
    
    def print_functions_directory(self) -> None:
        print(self.functions_directory)
        print('')

class Variables_Table:

    def __init__(self) -> None:
        columns = ['Name', 'Type', 'Kind', 'Virtual Direction', 'Dimension_one', 'Dimension_two']
        self.variables_table = pd.DataFrame(columns=columns)

    def push_variable(self, name: str, type: str, kind: str, virtual_direction: str, dimension_one:int = 1, dimension_two:int = 1) -> None:
        if type not in types:
            raise Exception(f'Unknown type: "{type}"')
        if self.lookup_variable(name):
            raise Exception(f'Identifier "{name}" is already declared!')
        new_variable = pd.DataFrame(
            {
                'Name': name,
                'Type': type,
                'Kind': kind,
                'Virtual Direction': virtual_direction,
                'Dimension_one': dimension_one,
                'Dimension_two': dimension_two,
            }, index=[0])
        self.variables_table = pd.concat([self.variables_table, new_variable], ignore_index=True)
    
    def lookup_variable(self, name: str) -> bool:
        return name in self.variables_table['Name'].values
    
    def get_variable(self, name: str, is_vm:bool=False) -> pd.DataFrame:
        variable = self.variables_table[self.variables_table['Name'] == name]
        if not variable.empty:
            return variable
        else:
            if is_vm:
                return variable
            else:
                raise Exception(f'Identifier "{name}" has not been declared!')
        
    def get_type(self, name: str) -> str:
        return self.get_variable(name).iloc[0]['Type']
    
    def get_dimension_one(self, name: str) -> str:
        return self.get_variable(name).iloc[0]['Dimension_one']
    
    def get_dimension_two(self, name: str) -> str:
        return self.get_variable(name).iloc[0]['Dimension_two']
    
    def print_variables_table(self) -> None:
        print(self.variables_table)
        print('')
    
    def get_virtual_memory(self, name: str) -> int:
        df = self.get_variable(name, is_vm=True)
        if df.empty:
            return -1
        else:
            return df.iloc[0]['Virtual Direction']
    
    def get_constant_dict(self) -> dict:
        filtered_df = self.variables_table[self.variables_table['Kind'] == 'const']
        constant_dict = filtered_df.set_index('Virtual Direction')['Name'].to_dict()
        return constant_dict

    def get_types_counter_list(self, is_local:bool=False) -> str:
        types_count_list = []
        # global variables
        global_ints = 0
        global_floats = 0
        global_chars = 0
        global_booleans = 0
        # local variables
        local_ints = 0
        local_floats = 0
        local_chars = 0
        local_booleans = 0
        # constants
        constant_ints = 0
        constant_floats = 0
        constant_chars = 0
        constant_booleans = 0
        # temporals
        temporal_ints = 0
        temporal_floats = 0
        temporal_chars = 0
        temporal_booleans = 0
        
        for index, row in self.variables_table.iterrows():
            kind = row['Kind']
            type = row['Type']
            if type == 'int':
                if kind == 'var':
                    if is_local:
                        local_ints += 1 * row['Dimension_one'] * row['Dimension_two']
                    else:
                        global_ints += 1 * row['Dimension_one'] * row['Dimension_two']
                if kind == 'const':
                    constant_ints += 1
                if kind == 'temp':
                    temporal_ints += 1
            elif type == 'float':
                if kind == 'var':
                    if is_local:
                        local_floats += 1
                    else:
                        global_floats += 1
                if kind == 'const':
                    constant_floats += 1
                if kind == 'temp':
                    temporal_floats += 1
            elif type == 'char':
                if kind == 'var':
                    if is_local:
                        local_chars += 1
                    else:
                        global_chars += 1
                if kind == 'const':
                    constant_chars += 1
                if kind == 'temp':
                    temporal_chars += 1
            elif type == 'bool':
                if kind == 'var':
                    if is_local:
                        local_booleans += 1
                    else:
                        global_booleans += 1
                if kind == 'const':
                    constant_booleans += 1
                if kind == 'temp':
                    temporal_booleans += 1
        # global variables
        types_count_list.append(global_ints)
        types_count_list.append(global_floats)
        types_count_list.append(global_chars)
        types_count_list.append(global_booleans)
        # local variables
        types_count_list.append(local_ints)
        types_count_list.append(local_floats)
        types_count_list.append(local_chars)
        types_count_list.append(local_booleans)
        # constants
        types_count_list.append(constant_ints)
        types_count_list.append(constant_floats)
        types_count_list.append(constant_chars)
        types_count_list.append(constant_booleans)
        # temporals
        types_count_list.append(temporal_ints)
        types_count_list.append(temporal_floats)
        types_count_list.append(temporal_chars)
        types_count_list.append(temporal_booleans)
        # int, float, char, bool
        # [g_i, g_f, g_c, g_b, l_i, l_f, l_c, l_b, c_i, c_f, c_c, c_b, t_i, t_f, t_c, t_b]
        return str(types_count_list)
    
    def empty_variables_table(self) -> None:
        self.variables_table = self.variables_table.iloc[0:0]
