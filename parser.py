import ply.yacc as yacc
from lexer import tokens
from Semantics.semantics import Semantics

semantics = Semantics()

def p_PROGRAM(p):
    '''
    PROGRAM : PROG add_type ID add_id ';' save_id VARS_PRIME FUNCTION_PRIME VOID MAIN '{' VARS_PRIME BLOCK '}'
    '''
    pass

def p_add_id(p):
    '''add_id : '''
    semantics.add_id(p[-1])

def p_add_type(p):
    '''add_type : '''
    semantics.add_type(p[-1])

def p_save_id(p):
    '''save_id : '''
    semantics.save_id()

def p_VARS_PRIME(p):
    '''
    VARS_PRIME : VARS
               | empty
    '''
    pass

def p_FUNCTION_PRIME(p):
    '''
    FUNCTION_PRIME : FUNCTION FUNC_PRIME
                   | empty
    '''
    pass

def p_FUNC(p):
    '''
    FUNC_PRIME : FUNCTION FUNC_PRIME
         | empty
    '''
    pass

def p_VARS(p):
    '''
    VARS : VAR TIPO_COMP ID TIPO_PRIME ';'
         | VAR TIPO_SIMPLE ID ';'
         | VAR TIPO_SIMPLE ID '[' I_CONST ']' ';'
    '''
    pass

def p_TIPO_PRIME(p):
    '''
    TIPO_PRIME : ',' ID TIPO_PRIME
               | empty
    '''
    pass

def p_VARIABLE(p):
    '''
    VARIABLE : ID
             | ID '[' EXPRESSION ']'
    '''
    pass

def p_TIPO_SIMPLE(p):
    '''
    TIPO_SIMPLE : INT
                | FLOAT
                | CHAR
    '''
    pass

def p_TIPO_COMP(p):
    '''
    TIPO_COMP : DATAFRAME
    '''
    pass

def p_FUNCTION(p):
    '''
    FUNCTION : FUNC TIPO_SIMPLE ID '(' PARAM ')' '{' VARS_PRIME BLOCK RETURN EXPRESSION '}'
             | FUNC TIPO_SIMPLE ID '(' PARAM ')' '{' VARS_PRIME BLOCK RETURN VAR_CT '}'
             | FUNC VOID ID '(' PARAM ')' '{' VARS_PRIME BLOCK '}'
    '''
    pass

def p_PARAM(p):
    '''
    PARAM : TIPO_SIMPLE ID PARAM_PRIME
          | empty
    '''
    pass

def p_PARAM_PRIME(p):
    '''
    PARAM_PRIME : ',' TIPO_SIMPLE ID PARAM_PRIME
                | empty
    '''
    pass

def p_BLOCK(p):
    '''
    BLOCK : STATEMENT BLOCK
          | empty
    '''
    pass

def p_STATEMENT(p):
    '''
    STATEMENT : ASSIGNATION
              | FUNC_CALL
              | WRITE
              | CONDITION
              | WHILE_STMT
              | FOR_STMT
              | DESCRIBE_STMT
    '''
    pass

def p_ASSIGNATION(p):
    '''
    ASSIGNATION : VARIABLE '=' EXPRESSION
    '''
    pass

def p_FUNC_CALL(p):
    '''
    FUNC_CALL : ID '(' EXPRESSION FUNC_CALL_PRIME ')'
    '''
    pass

def p_FUNC_CALL_PRIME(p):
    '''
    FUNC_CALL_PRIME : EXPRESSION FUNC_CALL_PRIME
                    | empty
    '''
    pass

def p_WRITE(p):
    '''
    WRITE : PRINT '(' EXPRESSION WRITE_PRIME ')'
               | PRINT '(' TITLE WRITE_PRIME ')'
    '''
    pass

def p_WRITE_PRIME(p):
    '''
    WRITE_PRIME : ',' EXPRESSION WRITE_PRIME
                | ',' TITLE WRITE_PRIME
                | empty
    '''
    pass

def p_CONDITION(p):
    '''
    CONDITION : IF '(' EXPRESSION ')' '{' BLOCK '}' ELSE_STMT
    '''
    pass

def p_ELSE_STMT(p):
    '''
    ELSE_STMT : ELSE '{' BLOCK '}'
              | empty
    '''
    pass

def p_WHILE_STMT(p):
    '''
    WHILE_STMT : WHILE '(' EXPRESSION ')' '{' BLOCK '}'
    '''
    pass

def p_FOR_STMT(p):
    '''
    FOR_STMT : FOR ID '=' EXPRESSION TO EXPRESSION DO '{' BLOCK '}'
    '''
    pass

def p_DESCRIBE_STMT(p):
    '''
    DESCRIBE_STMT : ID '.' DESCRIBE '(' ')' 
    '''
    pass

def p_EXPRESSION(p):
    '''
    EXPRESSION : AND_EXP EXPRESSION_PRIME
    '''
    pass

def p_EXPRESSION_PRIME(p):
    '''
    EXPRESSION_PRIME : OR AND_EXP EXPRESSION_PRIME
                     | empty
    '''
    pass

def p_AND_EXP(p):
    '''
    AND_EXP : B_EXP AND_EXP_PRIME
    '''
    pass

def p_AND_EXP_PRIME(p):
    '''
    AND_EXP_PRIME : AND B_EXP AND_EXP_PRIME
                  | empty
    '''
    pass

def p_B_EXP(p):
    '''
    B_EXP : TRUE
          | FALSE
          | EXP B_EXP_PRIME
    '''
    pass

def p_B_EXP_PRIME(p):
    '''
    B_EXP_PRIME : '>' 
                | '<'
                | DIFFERENT
                | EQUAL
                | empty
    '''
    pass

def p_EXP(p):
    '''
    EXP : TERM EXP_PRIME
    '''
    pass

def p_EXP_PRIME(p):
    '''
    EXP_PRIME : '+' TERM EXP_PRIME
              | '-' TERM EXP_PRIME
              | empty
    '''
    pass

def p_TERM(p):
    '''
    TERM : FACTOR TERM_PRIME
    '''
    pass

def p_TERM_PRIME(p):
    '''
    TERM_PRIME : '*' FACTOR TERM_PRIME
                  | '/' FACTOR TERM_PRIME
                  | empty
    '''
    pass

def p_FACTOR(p):
    '''
    FACTOR : '(' EXPRESSION ')'
              | '*' VAR_CT
              | '/' VAR_CT
              | VAR_CT
    '''
    pass

def p_VAR_CT(p):
    '''
    VAR_CT : ID
           | I_CONST
           | F_CONST
           | C_CONST
    '''
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

def p_empty(p):
    'empty :'
    pass

# Build the parser
parser = yacc.yacc()

input_str = f"""program patito; var int myvariable; void main {{ }}"""
print(input_str)
parser.parse(input_str) 
print(f'id_queue: {semantics.id_queue}')
print(f'types_stack: {semantics.types_stack}')
print(f'operands_stack: {semantics.operands_stack}')
print(f'operators_stack: {semantics.operators_stack}')
i = 0
for quad in semantics.quadruples:
    print(f'{i}. {quad}')
    i += 1
