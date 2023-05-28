types = {
    'int': 'int',
    'float': 'float',
    'char': 'char',
    'bool': 'bool',
}

function_types = types | {
    'program': 'program',
    'void': 'void'
}

operations = {
        '=': '=',
        '+': '+',
        '-': '-',
        '*': '*',
        '/': '/',
        '&&': '&&',
        '||': '||',
        '==': '==',
        '!=': '!=',
        '>': '>',
        '<': '<',
        '<=':'<='
    }

class Semantic_Cube():

    semantic_cube = {
        'int': {
            'int': {
                '=': types['int'],
                '+': types['int'],
                '-': types['int'],
                '*': types['int'],
                '/': types['int'],
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': types['bool'],
                '!=': types['bool'],
                '>': types['bool'],
                '<': types['bool'],
                '<=': types['bool'],
            },
            'float': {
                '=': 'ERROR',
                '+': types['float'],
                '-': types['float'],
                '*': types['float'],
                '/': types['float'],
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': types['bool'],
                '<': types['bool'],
            },
            'char': {
                '=': 'ERROR',
                '+': types['char'],
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
            },
            'bool': {
                '=': 'ERROR',
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
            }
        },
        'float': {
            'int': {
                '=': types['float'],
                '+': types['float'],
                '-': types['float'],
                '*': types['float'],
                '/': types['float'],
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': types['bool'],
                '<': types['bool'],
            },
            'float': {
                '=': types['float'],
                '+': types['float'],
                '-': types['float'],
                '*': types['float'],
                '/': types['float'],
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': types['bool'],
                '!=': types['bool'],
                '>': types['bool'],
                '<': types['bool'],
            },
            'char': {
                '=': 'ERROR',
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
            },
            'bool': {
                '=': 'ERROR',
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
            }
        },
        'char': {
            'int': {
                '=': 'ERROR',
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
            },
            'float': {
                '=': 'ERROR',
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
            },
            'char': {
                '=': types['char'],
                '+': types['char'],
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
            },
            'bool': {
                '=': 'ERROR',
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
            }
        },
        'bool': {
            'int': {
                '=': 'ERROR',
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
            },
            'float': {
                '=': 'ERROR',
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
            },
            'char': {
                '=': 'ERROR',
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
            },
            'bool': {
                '=': types['bool'],
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': types['bool'],
                '||': types['bool'],
                '==': types['bool'],
                '!=': types['bool'],
                '>': 'ERROR',
                '<': 'ERROR',
            }
        }
    }

    def match_types(self, left_operand: str, right_operand: str, operator: str) -> str:
        if left_operand not in types:
            raise Exception(f'Unknown type: {left_operand}')    
        if right_operand not in types:
            raise Exception(f'Unknown type: {right_operand}')
        if operator not in operations:
            raise Exception(f'Unknown operator: {operator} ')
        result = self.semantic_cube[left_operand][right_operand][operator]
        if result == 'ERROR':
            raise Exception(f'Type mismatch: {left_operand} {operator} {right_operand}')
        return result