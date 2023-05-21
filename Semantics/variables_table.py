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
    
    def get_current_function(self) -> str:
        return self.functions_directory['Name'].iloc[-1]
    
    def push_variables_types_used(self, name:str ,types_array: str) -> None:
        self.functions_directory.loc[self.functions_directory['Name'] == name, 'Variables types used'] = types_array 
    
    def push_parameters(self, name:str ,parameters_list: str) -> None:
        self.functions_directory.loc[self.functions_directory['Name'] == name, 'Parameters'] = parameters_list 
    
    def print_functions_directory(self) -> None:
        print(self.functions_directory)

class Variables_Table:
    def __init__(self) -> None:
        columns = ['Name', 'Type']
        self.variables_table = pd.DataFrame(columns=columns)

    def push_variable(self, name: str, type: str) -> None:
        if type not in types:
            raise Exception(f'Unknown type: "{type}"')
        if self.lookup_variable(name):
            raise Exception(f'Identifier "{name}" is already declared!')
        new_variable = pd.DataFrame(
            {
                'Name': name,
                'Type': type,
            }, index=[0])
        self.variables_table = pd.concat([self.variables_table, new_variable], ignore_index=True)
    
    def lookup_variable(self, name: str) -> bool:
        return name in self.variables_table['Name'].values
    
    def get_variable(self, name: str) -> pd.DataFrame:
        variable = self.variables_table[self.variables_table['Name'] == name]
        if not variable.empty:
            return variable
        else:
            raise Exception(f'Identifier "{name}" has not been declared!')
        
    def get_type(self, name: str) -> str:
        return self.get_variable(name).iloc[0]['Type']
    
    def print_variables_table(self) -> None:
        print(self.variables_table)

    def get_types_counter_list(self) -> str:
        types_count_list = []
        types_count = self.variables_table['Type'].value_counts()
        if 'int' in types_count:
            types_count_list.append(types_count['int'])
        else:
            types_count_list.append(0)
        if 'float' in types_count:
            types_count_list.append(types_count['float'])
        else:
            types_count_list.append(0)
        if 'char' in types_count:
            types_count_list.append(types_count['char'])
        else:
            types_count_list.append(0)
        if 'bool' in types_count:
            types_count_list.append(types_count['bool'])
        else:
            types_count_list.append(0)
        return str(types_count_list)

    def empty_variables_table(self) -> None:
        self.variables_table = self.variables_table.iloc[0:0]
