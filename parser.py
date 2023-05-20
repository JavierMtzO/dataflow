import ply.yacc as yacc
from lexer import tokens
from Semantics.semantics import Semantics

semantics = Semantics()

def p_PROGRAM(p):
    '''
    PROGRAM : PROG add_type ID add_id ';' save_ids VARS_PRIME FUNCTION_PRIME VOID MAIN '{' VARS_PRIME BLOCK '}'
    '''
    pass

def p_add_id(p):
    '''add_id : '''
    semantics.add_id(p[-1])

def p_save_ids(p):
    '''save_ids : '''
    semantics.save_ids()

def p_VARS_PRIME(p):
    '''
    VARS_PRIME : VARS VARS_PRIME
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

def p_add_type(p):
    '''add_type : '''
    semantics.add_type(p[-1], True)

def p_add_current_type(p):
    '''add_current_type : '''
    semantics.add_type(semantics.current_type, False)

def p_VARS(p):
    '''
    VARS : VAR TIPO_COMP ID add_id TIPO_PRIME ';' save_ids
         | VAR TIPO_SIMPLE ID add_id TIPO_PRIME ';' save_ids
         | VAR TIPO_SIMPLE ID '[' EXPRESSION ']' ';'
         | VAR TIPO_SIMPLE ID '[' EXPRESSION ']' '[' EXPRESSION ']' ';'
    '''
    pass

def p_TIPO_PRIME(p):
    '''
    TIPO_PRIME : ',' ID add_id add_current_type TIPO_PRIME
               | empty
    '''
    pass

def p_get_variable(p):
    '''get_variable : '''
    semantics.get_variable(p[-1])

def p_VARIABLE(p):
    '''
    VARIABLE : ID get_variable
             | ID '[' EXPRESSION ']'
    '''
    pass

def p_TIPO_SIMPLE(p):
    '''
    TIPO_SIMPLE : INT add_type
                | FLOAT add_type
                | CHAR add_type
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
              | EXPRESSION ';'
              | WRITE ';'
              | CONDITION
              | WHILE_STMT
              | FOR_STMT
              | DESCRIBE_STMT
    '''
    pass

def p_add_operator(p):
    '''add_operator : '''
    semantics.add_operator(p[-1]) 

def p_add_operand(p):
    '''add_operand : '''
    semantics.add_operand(p[-1])

def p_add_assignation_quad(p):
    '''add_assignation_quad : '''
    semantics.assignment_quad()

def p_add_assignation_for_quad(p):
    '''add_assignation_for_quad : '''
    semantics.assignment_quad(is_for=True)

def p_ASSIGNATION(p):
    '''
    ASSIGNATION : VARIABLE '=' add_operator EXPRESSION ';' add_assignation_quad
                | FOR VARIABLE '=' add_operator EXPRESSION add_assignation_for_quad
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

def p_print_quad(p):
    '''print_quad : '''
    semantics.print_quad()

def p_add_print_operator(p):
    '''add_print_operator : '''
    semantics.add_operator('print') 

def p_WRITE(p):
    '''
    WRITE : PRINT add_operator '(' EXPRESSION print_quad WRITE_PRIME ')'
               | PRINT add_operator '(' TITLE WRITE_PRIME ')'
    '''
    pass

def p_WRITE_PRIME(p):
    '''
    WRITE_PRIME : ',' add_print_operator EXPRESSION print_quad WRITE_PRIME
                | ',' add_print_operator TITLE print_quad WRITE_PRIME
                | empty
    '''
    pass

def p_go_to_false_quad(p):
    '''go_to_false_quad : '''
    semantics.go_to_false_quad() 

def p_fill_go_to_false_quad(p):
    '''fill_go_to_false_quad : '''
    semantics.fill_go_to_false_quad() 

def p_go_to_true_quad(p):
    '''go_to_true_quad : '''
    semantics.go_to_true_quad() 

def p_fill_go_to_true_quad(p):
    '''fill_go_to_true_quad : '''
    semantics.fill_go_to_true_quad() 

def p_go_to_quad(p):
    '''go_to_quad : '''
    semantics.go_to_quad() 

def p_pop_operand(p):
    '''pop_operand : '''
    semantics.pop_operand() 

def p_pop_type(p):
    '''pop_type : '''
    semantics.pop_type() 

def p_append_jump(p):
    '''append_jump : '''
    semantics.append_jump() 

def p_CONDITION(p):
    '''
    CONDITION : IF '(' EXPRESSION pop_operand pop_type ')' '{' go_to_false_quad BLOCK '}' fill_go_to_false_quad ELSE_STMT
    '''
    pass

def p_ELSE_STMT(p):
    '''
    ELSE_STMT : ELSE '{' go_to_true_quad BLOCK '}' fill_go_to_true_quad
              | empty
    '''
    pass

def p_WHILE_STMT(p):
    '''
    WHILE_STMT : WHILE '(' append_jump EXPRESSION pop_operand pop_type ')' '{' go_to_false_quad  BLOCK '}' fill_go_to_false_quad go_to_quad
    '''
    pass

def p_check_exact_type_for(p):
    '''check_exact_type_for : '''
    semantics.check_exact_type_for(type='int') 

def p_add_final_counter_for(p):
    '''add_final_counter_for : '''
    semantics.add_final_counter_for()

def p_generate_for_quad(p):
    '''generate_for_quad : '''
    semantics.generate_for_quad()

def p_check_boolean_expression_for(p):
    '''check_boolean_expression_for : '''
    semantics.check_boolean_expression_for()

def p_end_for(p):
    '''end_for : '''
    semantics.end_for()

def p_FOR_STMT(p):
    '''
    FOR_STMT : ASSIGNATION check_exact_type_for TO '(' EXPRESSION check_exact_type_for add_final_counter_for check_boolean_expression_for ')' generate_for_quad DO '{' BLOCK '}' end_for
    '''
    pass

def p_DESCRIBE_STMT(p):
    '''
    DESCRIBE_STMT : ID '.' DESCRIBE '(' ')' 
    '''
    pass

def p_aritmetics_operation(p):
    '''aritmetics_operation : '''
    semantics.aritmetics_operation()

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
    B_EXP_PRIME : '>' add_operator B_EXP aritmetics_operation
                | '<' add_operator B_EXP aritmetics_operation
                | DIFFERENT add_operator B_EXP aritmetics_operation
                | EQUAL add_operator B_EXP aritmetics_operation
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
    EXP_PRIME : '+' add_operator TERM EXP_PRIME aritmetics_operation
              | '-' add_operator TERM EXP_PRIME aritmetics_operation
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
    TERM_PRIME : '*' add_operator FACTOR aritmetics_operation TERM_PRIME 
                  | '/' add_operator FACTOR aritmetics_operation TERM_PRIME 
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
    VAR_CT : ID add_operand
           | I_CONST add_operand
           | F_CONST add_operand
           | C_CONST add_operand
    '''
    pass

# Error rule for syntax errors
def p_error(p):
    raise Exception(f'Syntax error in input!')

def p_empty(p):
    'empty :'
    pass

# Build the parser
parser = yacc.yacc()

######### TEST #############
with open('./Pruebas/sample_program.df', 'r') as file:
    dataflow_file = file.read()
parser.parse(dataflow_file) 
print(f'id_queue: {semantics.id_queue}')
print(f'types_stack: {semantics.types_stack}')
print(f'operands_stack: {semantics.operands_stack}')
print(f'operators_stack: {semantics.operators_stack}')
print(f'for_vc_stack: {semantics.for_vc_stack}')
print(f'for_vf_stack: {semantics.for_vf_stack}')
print(f'jumps_stack: {semantics.jumps_stack}')
print('Quadruples:')
i = 0
for quad in semantics.quadruples:
    print(f'{i}. {quad.print_quadruple()}')
    i+=1
print('Variables table:')
semantics.variables_table.print_variables_table()
############################