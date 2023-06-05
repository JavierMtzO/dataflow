import ply.yacc as yacc
from lexer import tokens
from Semantics.semantics import Semantics

semantics = Semantics()

"""
This file defines the syntax and semantics for a 
Dataflow language using the PLY (Python Lex-Yacc) library.

"""

def p_PROGRAM(p):
    '''
    PROGRAM : PROG add_type ID add_id ';' go_to_main save_function VARS_PRIME FUNCTION_PRIME VOID MAIN '{' fill_go_to_main_quad VARS_PRIME BLOCK '}' empty_global_variables_table
    '''
    pass

def p_go_to_main(p):
    '''go_to_main : '''
    semantics.go_to_main()

def p_empty_global_variables_table(p):
    '''empty_global_variables_table : '''
    semantics.empty_variables_table()

def p_empty_local_variables_table(p):
    '''empty_local_variables_table : '''
    semantics.empty_variables_table(is_local=True)

def p_fill_go_to_main_quad(p):
    '''fill_go_to_main_quad : '''
    semantics.fill_go_to_main_quad()

def p_add_id(p):
    '''add_id : '''
    semantics.add_id(p[-1])

def p_save_ids(p):
    '''save_ids : '''
    semantics.save_ids()

def p_save_parameter(p):
    '''save_parameter : '''
    semantics.save_ids(is_parameter=True)

def p_save_function(p):
    '''save_function : '''
    semantics.save_function()

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

def p_check_for_array_length(p):
    '''check_for_array_length : '''
    semantics.check_for_array_length()

def p_save_array(p):
    '''save_array : '''
    semantics.save_array()

def p_save_matrix(p):
    '''save_matrix : '''
    semantics.save_matrix()

def p_VARS(p):
    '''
    VARS : VAR TIPO_COMP ID add_id TIPO_PRIME ';' save_ids
         | VAR TIPO_SIMPLE ID add_id TIPO_PRIME ';' save_ids
         | VAR TIPO_SIMPLE ID add_id '[' EXPRESSION ']' check_for_array_length ';' save_array
         | VAR TIPO_SIMPLE ID add_id '[' EXPRESSION ']' check_for_array_length '[' EXPRESSION ']' check_for_array_length ';' save_matrix
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

def p_ver_quad_dimension_one_array(p):
    '''ver_quad_dimension_one_array : '''
    semantics.ver_quad_dimension_one_array()

def p_ver_quad_dimension_one_matrix(p):
    '''ver_quad_dimension_one_matrix : '''
    semantics.ver_quad_dimension_one_matrix()

def p_ver_quad_dimension_two_matrix(p):
    '''ver_quad_dimension_two_matrix : '''
    semantics.ver_quad_dimension_two_matrix()

def p_VARIABLE(p):
    '''
    VARIABLE : ID get_variable
             | ID add_id '[' EXPRESSION ']' ver_quad_dimension_one_array
             | ID add_id '[' EXPRESSION ']' ver_quad_dimension_one_matrix '[' EXPRESSION ']' ver_quad_dimension_two_matrix
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

def p_add_function_type(p):
    '''add_function_type : '''
    semantics.add_function_type()

def p_save_function_as_variable(p):
    '''save_function_as_variable : '''
    semantics.save_function_as_variable()

def p_return_quad(p):
    '''return_quad : '''
    semantics.return_quad()

def p_FUNCTION(p):
    '''
    FUNCTION : FUNC TIPO_SIMPLE add_function_type ID add_id save_function '(' PARAM add_parameters ')' save_function_as_variable '{' VARS_PRIME BLOCK RETURN EXPRESSION ';' return_quad '}' empty_local_variables_table
             | FUNC VOID add_type ID add_id save_function '(' PARAM add_parameters ')' '{' VARS_PRIME BLOCK '}' empty_local_variables_table
    '''
    pass

def p_add_parameters(p):
    '''add_parameters : '''
    semantics.add_parameters()

def p_PARAM(p):
    '''
    PARAM : TIPO_SIMPLE ID add_id save_parameter PARAM_PRIME
          | empty
    '''
    pass

def p_PARAM_PRIME(p):
    '''
    PARAM_PRIME : ',' TIPO_SIMPLE ID add_id save_parameter PARAM_PRIME
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

def p_functions_assignation(p):
    '''functions_assignation : '''
    semantics.functions_assignation()

def p_ASSIGNATION(p):
    '''
    ASSIGNATION : VARIABLE '=' add_operator EXPRESSION ';' add_assignation_quad
                | FOR VARIABLE '=' add_operator EXPRESSION add_assignation_for_quad
                | VARIABLE '=' add_operator FUNC_CALL functions_assignation add_assignation_quad
    '''
    pass

def p_era_quad(p):
    '''era_quad : '''
    semantics.era_quad(p[-1])

def p_param_quad(p):
    '''param_quad : '''
    semantics.param_quad()

def p_go_sub_quad(p):
    '''go_sub_quad : '''
    semantics.go_sub_quad()

def p_FUNC_CALL(p):
    '''
    FUNC_CALL : FUNC ID era_quad '(' EXPRESSION param_quad FUNC_CALL_PRIME ')' go_sub_quad
    '''
    pass

def p_FUNC_CALL_PRIME(p):
    '''
    FUNC_CALL_PRIME : ',' EXPRESSION param_quad FUNC_CALL_PRIME
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

def p_fill_go_to_false_quad_if(p):
    '''fill_go_to_false_quad_if : '''
    semantics.fill_go_to_false_quad(jumps=0) 

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
    CONDITION : IF '(' EXPRESSION pop_type ')' '{' go_to_false_quad BLOCK '}' fill_go_to_false_quad_if ELSE_STMT
    '''
    pass

def p_ELSE_STMT(p):
    '''
    ELSE_STMT : ELSE '{' go_to_true_quad BLOCK '}' fill_go_to_true_quad
              | empty pop_operand
    '''
    pass

def p_WHILE_STMT(p):
    '''
    WHILE_STMT : WHILE '(' append_jump EXPRESSION pop_type ')' '{' go_to_false_quad  BLOCK '}' fill_go_to_false_quad go_to_quad pop_operand
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
           | FUNC_CALL
           | ID add_id '[' EXPRESSION ']' ver_quad_dimension_one_array
           | ID add_id '[' EXPRESSION ']' ver_quad_dimension_one_matrix '[' EXPRESSION ']' ver_quad_dimension_two_matrix
    '''
    pass

# Error rule for syntax errors
def p_error(p):
    raise Exception(f'Syntax error in input!')

def p_empty(p):
    'empty :'
    pass

# Build the parser
dataflow_parser = yacc.yacc()