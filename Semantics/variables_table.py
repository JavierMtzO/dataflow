import pandas as pd
from Semantics.semantic_cube import types

class Variables_Table:
    def __init__(self) -> None:
        columns = ['Name', 'Type', 'Value']
        self.variables_table = pd.DataFrame(columns=columns)

    def push_variable(self, name: str, type: str, value:str = None) -> None:
        if type not in types:
            raise Exception(f'Unknown type: "{type}"')
        if self.lookup_variable(name):
            raise Exception(f'Identifier "{name}" is already declared!')
        new_variable = pd.DataFrame(
            {
                'Name': name,
                'Type': type,
                'Value': value,
            }, index=[0])
        self.variables_table = pd.concat([self.variables_table, new_variable], ignore_index=True)
    
    def lookup_variable(self, name: str) -> bool:
        return name in self.variables_table['Name'].values
    
    def get_variable(self, name: str) -> pd.DataFrame:
        return self.variables_table[self.variables_table['Name'] == name]
    
    def change_variable_value(self, name: str, new_value) -> None:
        self.variables_table.loc[self.variables_table['Name'] == name, 'Value'] = new_value
    
    def get_type(self, name: str) -> str:
        return self.get_variable(name).iloc[0]['Type']
    
    def print_variables_table(self):
        print(self.variables_table)