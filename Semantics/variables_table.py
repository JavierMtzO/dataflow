from Semantics.semantic_cube import types

class Variables_Table_Initiation:
    def __init__(self, type: str) -> None:
        self.type = type

class Variables_Table:
    def __init__(self) -> None:
        self.variables_table = {}

    def push_variable(self, name: str, type: str) -> None:
        if type not in types:
            raise Exception('Unknown type!')
        if name in self.variables_table:
            raise Exception('Identifier is already declared!')
        self.variables_table[name] = Variables_Table_Initiation(types[type])