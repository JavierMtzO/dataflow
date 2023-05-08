
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND CHAR C_CONST DATAFRAME DESCRIBE DIFFERENT DO ELSE EQUAL FALSE FLOAT FOR FUNC F_CONST ID IF INT I_CONST MAIN OR PRINT PROG RETURN TITLE TO TRUE VAR VOID WHILE\n    PROGRAM : PROG add_type ID add_id ';' save_id VARS_PRIME FUNCTION_PRIME VOID MAIN '{' VARS_PRIME BLOCK '}'\n    add_id : add_type : save_id : \n    VARS_PRIME : VARS\n               | empty\n    \n    FUNCTION_PRIME : FUNCTION FUNC_PRIME\n                   | empty\n    \n    FUNC_PRIME : FUNCTION FUNC_PRIME\n         | empty\n    \n    VARS : VAR TIPO_COMP ID TIPO_PRIME ';'\n         | VAR TIPO_SIMPLE ID ';'\n         | VAR TIPO_SIMPLE ID '[' I_CONST ']' ';'\n    \n    TIPO_PRIME : ',' ID TIPO_PRIME\n               | empty\n    \n    VARIABLE : ID\n             | ID '[' EXPRESSION ']'\n    \n    TIPO_SIMPLE : INT\n                | FLOAT\n                | CHAR\n    \n    TIPO_COMP : DATAFRAME\n    \n    FUNCTION : FUNC TIPO_SIMPLE ID '(' PARAM ')' '{' VARS_PRIME BLOCK RETURN EXPRESSION '}'\n             | FUNC TIPO_SIMPLE ID '(' PARAM ')' '{' VARS_PRIME BLOCK RETURN VAR_CT '}'\n             | FUNC VOID ID '(' PARAM ')' '{' VARS_PRIME BLOCK '}'\n    \n    PARAM : TIPO_SIMPLE ID PARAM_PRIME\n          | empty\n    \n    PARAM_PRIME : ',' TIPO_SIMPLE ID PARAM_PRIME\n                | empty\n    \n    BLOCK : STATEMENT BLOCK\n          | empty\n    \n    STATEMENT : ASSIGNATION\n              | FUNC_CALL\n              | WRITE\n              | CONDITION\n              | WHILE_STMT\n              | FOR_STMT\n              | DESCRIBE_STMT\n    \n    ASSIGNATION : VARIABLE '=' EXPRESSION\n    \n    FUNC_CALL : ID '(' EXPRESSION FUNC_CALL_PRIME ')'\n    \n    FUNC_CALL_PRIME : EXPRESSION FUNC_CALL_PRIME\n                    | empty\n    \n    WRITE : PRINT '(' EXPRESSION WRITE_PRIME ')'\n               | PRINT '(' TITLE WRITE_PRIME ')'\n    \n    WRITE_PRIME : ',' EXPRESSION WRITE_PRIME\n                | ',' TITLE WRITE_PRIME\n                | empty\n    \n    CONDITION : IF '(' EXPRESSION ')' '{' BLOCK '}' ELSE_STMT\n    \n    ELSE_STMT : ELSE '{' BLOCK '}'\n              | empty\n    \n    WHILE_STMT : WHILE '(' EXPRESSION ')' '{' BLOCK '}'\n    \n    FOR_STMT : FOR ID '=' EXPRESSION TO EXPRESSION DO '{' BLOCK '}'\n    \n    DESCRIBE_STMT : ID '.' DESCRIBE '(' ')' \n    \n    EXPRESSION : AND_EXP EXPRESSION_PRIME\n    \n    EXPRESSION_PRIME : OR AND_EXP EXPRESSION_PRIME\n                     | empty\n    \n    AND_EXP : B_EXP AND_EXP_PRIME\n    \n    AND_EXP_PRIME : AND B_EXP AND_EXP_PRIME\n                  | empty\n    \n    B_EXP : TRUE\n          | FALSE\n          | EXP B_EXP_PRIME\n    \n    B_EXP_PRIME : '>' \n                | '<'\n                | DIFFERENT\n                | EQUAL\n                | empty\n    \n    EXP : TERM EXP_PRIME\n    \n    EXP_PRIME : '+' TERM EXP_PRIME\n              | '-' TERM EXP_PRIME\n              | empty\n    \n    TERM : FACTOR TERM_PRIME\n    \n    TERM_PRIME : '*' FACTOR TERM_PRIME\n                  | '/' FACTOR TERM_PRIME\n                  | empty\n    \n    FACTOR : '(' EXPRESSION ')'\n              | '*' VAR_CT\n              | '/' VAR_CT\n              | VAR_CT\n    \n    VAR_CT : ID\n           | I_CONST\n           | F_CONST\n           | C_CONST\n    empty :"
    
_lr_action_items = {'PROG':([0,],[2,]),'$end':([1,75,],[0,-1,]),'ID':([2,3,9,10,16,17,18,19,20,21,26,27,35,37,39,42,45,46,54,56,57,58,59,60,61,62,67,71,72,74,77,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,105,110,111,112,113,115,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,143,152,154,155,156,157,158,159,160,161,162,165,166,167,168,170,172,173,174,175,176,177,185,186,190,192,193,194,197,198,],[-3,4,-5,-6,28,29,-21,-18,-19,-20,32,33,43,-12,-83,-11,52,68,52,-31,-32,-33,-34,-35,-36,-37,81,-13,87,87,87,87,87,87,-83,-83,-79,87,87,-83,-83,-59,-60,-83,-83,-83,87,-78,87,-80,-81,-82,-38,87,149,52,52,87,-53,87,-55,-56,87,-58,-61,-62,-63,-64,-65,-66,-67,87,87,-70,-71,87,87,-74,-76,-77,87,-75,-39,-83,-83,-83,-83,-83,-83,-52,-42,-43,52,52,87,87,-54,-57,-68,-69,-72,-73,-83,-50,-47,-49,52,52,-51,-48,]),';':([4,5,28,29,34,36,43,50,51,],[-2,6,-83,37,42,-15,-83,-14,71,]),'VAR':([6,7,39,85,86,],[-4,11,11,11,11,]),'FUNC':([6,7,8,9,10,13,23,37,42,71,171,188,189,],[-4,-83,15,-5,-6,15,15,-12,-11,-13,-24,-22,-23,]),'VOID':([6,7,8,9,10,12,13,14,15,23,24,25,31,37,42,71,171,188,189,],[-4,-83,-83,-5,-6,22,-83,-8,27,-83,-7,-10,-9,-12,-11,-13,-24,-22,-23,]),'PRINT':([9,10,37,39,42,45,54,56,57,58,59,60,61,62,71,85,86,87,90,91,92,93,94,95,96,98,100,101,102,105,112,113,118,120,121,123,124,125,126,127,128,129,130,133,134,137,138,139,152,154,155,156,157,158,159,160,161,162,165,166,167,172,173,174,175,176,177,185,186,190,192,193,194,197,198,],[-5,-6,-12,-83,-11,64,64,-31,-32,-33,-34,-35,-36,-37,-13,-83,-83,-79,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,-38,64,64,-53,-55,-56,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,-75,-39,-83,-83,-83,-83,-83,-83,-52,-42,-43,64,64,-54,-57,-68,-69,-72,-73,-83,-50,-47,-49,64,64,-51,-48,]),'IF':([9,10,37,39,42,45,54,56,57,58,59,60,61,62,71,85,86,87,90,91,92,93,94,95,96,98,100,101,102,105,112,113,118,120,121,123,124,125,126,127,128,129,130,133,134,137,138,139,152,154,155,156,157,158,159,160,161,162,165,166,167,172,173,174,175,176,177,185,186,190,192,193,194,197,198,],[-5,-6,-12,-83,-11,65,65,-31,-32,-33,-34,-35,-36,-37,-13,-83,-83,-79,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,-38,65,65,-53,-55,-56,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,-75,-39,-83,-83,-83,-83,-83,-83,-52,-42,-43,65,65,-54,-57,-68,-69,-72,-73,-83,-50,-47,-49,65,65,-51,-48,]),'WHILE':([9,10,37,39,42,45,54,56,57,58,59,60,61,62,71,85,86,87,90,91,92,93,94,95,96,98,100,101,102,105,112,113,118,120,121,123,124,125,126,127,128,129,130,133,134,137,138,139,152,154,155,156,157,158,159,160,161,162,165,166,167,172,173,174,175,176,177,185,186,190,192,193,194,197,198,],[-5,-6,-12,-83,-11,66,66,-31,-32,-33,-34,-35,-36,-37,-13,-83,-83,-79,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,-38,66,66,-53,-55,-56,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,-75,-39,-83,-83,-83,-83,-83,-83,-52,-42,-43,66,66,-54,-57,-68,-69,-72,-73,-83,-50,-47,-49,66,66,-51,-48,]),'FOR':([9,10,37,39,42,45,54,56,57,58,59,60,61,62,71,85,86,87,90,91,92,93,94,95,96,98,100,101,102,105,112,113,118,120,121,123,124,125,126,127,128,129,130,133,134,137,138,139,152,154,155,156,157,158,159,160,161,162,165,166,167,172,173,174,175,176,177,185,186,190,192,193,194,197,198,],[-5,-6,-12,-83,-11,67,67,-31,-32,-33,-34,-35,-36,-37,-13,-83,-83,-79,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,-38,67,67,-53,-55,-56,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,-75,-39,-83,-83,-83,-83,-83,-83,-52,-42,-43,67,67,-54,-57,-68,-69,-72,-73,-83,-50,-47,-49,67,67,-51,-48,]),'}':([9,10,37,39,42,45,53,54,55,56,57,58,59,60,61,62,71,76,86,87,90,91,92,93,94,95,96,98,100,101,102,105,113,118,120,121,123,124,125,126,127,128,129,130,133,134,137,138,139,151,152,154,155,156,157,158,159,160,161,162,165,166,167,172,173,174,175,176,177,180,181,183,184,185,186,190,192,193,194,195,196,197,198,],[-5,-6,-12,-83,-11,-83,75,-83,-30,-31,-32,-33,-34,-35,-36,-37,-13,-29,-83,-79,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,-38,-83,-53,-55,-56,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,171,-75,-39,-83,-83,-83,-83,-83,-83,-52,-42,-43,-83,-83,-54,-57,-68,-69,-72,-73,185,186,188,189,-83,-50,-47,-49,-83,-83,197,198,-51,-48,]),'RETURN':([9,10,37,42,54,55,56,57,58,59,60,61,62,71,76,85,87,90,91,92,93,94,95,96,98,100,101,102,105,112,118,120,121,123,124,125,126,127,128,129,130,133,134,137,138,139,150,152,154,155,156,157,158,159,160,161,162,165,172,173,174,175,176,177,185,186,190,192,197,198,],[-5,-6,-12,-11,-83,-30,-31,-32,-33,-34,-35,-36,-37,-13,-29,-83,-79,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,-38,-83,-53,-55,-56,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,170,-75,-39,-83,-83,-83,-83,-83,-83,-52,-42,-43,-54,-57,-68,-69,-72,-73,-83,-50,-47,-49,-51,-48,]),'DATAFRAME':([11,],[18,]),'INT':([11,15,40,41,83,],[19,19,19,19,19,]),'FLOAT':([11,15,40,41,83,],[20,20,20,20,20,]),'CHAR':([11,15,40,41,83,],[21,21,21,21,21,]),'MAIN':([22,],[30,]),',':([28,43,68,87,90,91,92,93,94,95,96,98,100,101,102,106,107,118,120,121,123,124,125,126,127,128,129,130,133,134,137,138,139,149,152,155,156,157,158,159,160,163,164,172,173,174,175,176,177,],[35,35,83,-79,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,143,143,-53,-55,-56,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,83,-75,-83,-83,-83,-83,-83,-83,143,143,-54,-57,-68,-69,-72,-73,]),'[':([29,52,],[38,74,]),'{':([30,69,70,146,147,187,191,],[39,85,86,166,167,193,194,]),'(':([32,33,52,64,65,66,72,74,77,78,79,80,87,88,89,90,91,92,93,94,95,96,98,100,101,102,103,110,115,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,143,152,155,156,157,158,159,160,168,170,172,173,174,175,176,177,],[40,41,72,78,79,80,88,88,88,88,88,88,-79,88,88,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,140,88,88,-53,88,-55,-56,88,-58,-61,-62,-63,-64,-65,-66,-67,88,88,-70,-71,88,88,-74,-76,-77,88,-75,-83,-83,-83,-83,-83,-83,88,88,-54,-57,-68,-69,-72,-73,]),'I_CONST':([38,72,74,77,78,79,80,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,110,115,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,143,152,155,156,157,158,159,160,168,170,172,173,174,175,176,177,],[44,100,100,100,100,100,100,-79,100,100,-83,-83,-59,-60,-83,-83,-83,100,-78,100,-80,-81,-82,100,100,-53,100,-55,-56,100,-58,-61,-62,-63,-64,-65,-66,-67,100,100,-70,-71,100,100,-74,-76,-77,100,-75,-83,-83,-83,-83,-83,-83,100,100,-54,-57,-68,-69,-72,-73,]),')':([40,41,47,48,49,68,82,84,87,89,90,91,92,93,94,95,96,98,100,101,102,106,107,108,109,114,115,116,117,118,120,121,123,124,125,126,127,128,129,130,133,134,137,138,139,140,142,144,145,149,152,153,155,156,157,158,159,160,163,164,169,172,173,174,175,176,177,178,179,],[-83,-83,69,-26,70,-83,-25,-28,-79,-83,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,-83,-83,146,147,152,-83,154,-41,-53,-55,-56,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,161,162,-46,165,-83,-75,-40,-83,-83,-83,-83,-83,-83,-83,-83,-27,-54,-57,-68,-69,-72,-73,-44,-45,]),']':([44,87,90,91,92,93,94,95,96,98,100,101,102,104,118,120,121,123,124,125,126,127,128,129,130,133,134,137,138,139,152,155,156,157,158,159,160,172,173,174,175,176,177,],[51,-79,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,141,-53,-55,-56,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,-75,-83,-83,-83,-83,-83,-83,-54,-57,-68,-69,-72,-73,]),'.':([52,],[73,]),'=':([52,63,81,141,],[-16,77,110,-17,]),'TRUE':([72,74,77,78,79,80,87,88,89,90,91,92,93,94,95,96,98,100,101,102,110,115,118,119,120,121,122,123,124,125,126,127,128,129,130,133,134,137,138,139,143,152,155,156,157,158,159,160,168,170,172,173,174,175,176,177,],[92,92,92,92,92,92,-79,92,92,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,92,92,-53,92,-55,-56,92,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,92,-75,-83,-83,-83,-83,-83,-83,92,92,-54,-57,-68,-69,-72,-73,]),'FALSE':([72,74,77,78,79,80,87,88,89,90,91,92,93,94,95,96,98,100,101,102,110,115,118,119,120,121,122,123,124,125,126,127,128,129,130,133,134,137,138,139,143,152,155,156,157,158,159,160,168,170,172,173,174,175,176,177,],[93,93,93,93,93,93,-79,93,93,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,93,93,-53,93,-55,-56,93,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,93,-75,-83,-83,-83,-83,-83,-83,93,93,-54,-57,-68,-69,-72,-73,]),'*':([72,74,77,78,79,80,87,88,89,90,91,92,93,94,95,96,98,100,101,102,110,115,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,143,152,155,156,157,158,159,160,168,170,172,173,174,175,176,177,184,],[97,97,97,97,97,97,-79,97,97,-83,-83,-59,-60,-83,-83,135,-78,-80,-81,-82,97,97,-53,97,-55,-56,97,-58,-61,-62,-63,-64,-65,-66,-67,97,97,-70,-71,97,97,-74,-76,-77,97,-75,-83,-83,-83,-83,135,135,97,97,-54,-57,-68,-69,-72,-73,-78,]),'/':([72,74,77,78,79,80,87,88,89,90,91,92,93,94,95,96,98,100,101,102,110,115,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,143,152,155,156,157,158,159,160,168,170,172,173,174,175,176,177,184,],[99,99,99,99,99,99,-79,99,99,-83,-83,-59,-60,-83,-83,136,-78,-80,-81,-82,99,99,-53,99,-55,-56,99,-58,-61,-62,-63,-64,-65,-66,-67,99,99,-70,-71,99,99,-74,-76,-77,99,-75,-83,-83,-83,-83,136,136,99,99,-54,-57,-68,-69,-72,-73,-78,]),'F_CONST':([72,74,77,78,79,80,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,110,115,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,143,152,155,156,157,158,159,160,168,170,172,173,174,175,176,177,],[101,101,101,101,101,101,-79,101,101,-83,-83,-59,-60,-83,-83,-83,101,-78,101,-80,-81,-82,101,101,-53,101,-55,-56,101,-58,-61,-62,-63,-64,-65,-66,-67,101,101,-70,-71,101,101,-74,-76,-77,101,-75,-83,-83,-83,-83,-83,-83,101,101,-54,-57,-68,-69,-72,-73,]),'C_CONST':([72,74,77,78,79,80,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,110,115,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,143,152,155,156,157,158,159,160,168,170,172,173,174,175,176,177,],[102,102,102,102,102,102,-79,102,102,-83,-83,-59,-60,-83,-83,-83,102,-78,102,-80,-81,-82,102,102,-53,102,-55,-56,102,-58,-61,-62,-63,-64,-65,-66,-67,102,102,-70,-71,102,102,-74,-76,-77,102,-75,-83,-83,-83,-83,-83,-83,102,102,-54,-57,-68,-69,-72,-73,]),'DESCRIBE':([73,],[103,]),'TITLE':([78,143,],[107,164,]),'+':([87,95,96,98,100,101,102,134,137,138,139,152,157,158,159,160,176,177,184,],[-79,131,-83,-78,-80,-81,-82,-71,-74,-76,-77,-75,131,131,-83,-83,-72,-73,-78,]),'-':([87,95,96,98,100,101,102,134,137,138,139,152,157,158,159,160,176,177,184,],[-79,132,-83,-78,-80,-81,-82,-71,-74,-76,-77,-75,132,132,-83,-83,-72,-73,-78,]),'>':([87,94,95,96,98,100,101,102,130,133,134,137,138,139,152,157,158,159,160,174,175,176,177,184,],[-79,125,-83,-83,-78,-80,-81,-82,-67,-70,-71,-74,-76,-77,-75,-83,-83,-83,-83,-68,-69,-72,-73,-78,]),'<':([87,94,95,96,98,100,101,102,130,133,134,137,138,139,152,157,158,159,160,174,175,176,177,184,],[-79,126,-83,-83,-78,-80,-81,-82,-67,-70,-71,-74,-76,-77,-75,-83,-83,-83,-83,-68,-69,-72,-73,-78,]),'DIFFERENT':([87,94,95,96,98,100,101,102,130,133,134,137,138,139,152,157,158,159,160,174,175,176,177,184,],[-79,127,-83,-83,-78,-80,-81,-82,-67,-70,-71,-74,-76,-77,-75,-83,-83,-83,-83,-68,-69,-72,-73,-78,]),'EQUAL':([87,94,95,96,98,100,101,102,130,133,134,137,138,139,152,157,158,159,160,174,175,176,177,184,],[-79,128,-83,-83,-78,-80,-81,-82,-67,-70,-71,-74,-76,-77,-75,-83,-83,-83,-83,-68,-69,-72,-73,-78,]),'AND':([87,91,92,93,94,95,96,98,100,101,102,124,125,126,127,128,129,130,133,134,137,138,139,152,156,157,158,159,160,174,175,176,177,184,],[-79,122,-59,-60,-83,-83,-83,-78,-80,-81,-82,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,-75,122,-83,-83,-83,-83,-68,-69,-72,-73,-78,]),'OR':([87,90,91,92,93,94,95,96,98,100,101,102,121,123,124,125,126,127,128,129,130,133,134,137,138,139,152,155,156,157,158,159,160,173,174,175,176,177,184,],[-79,119,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,-56,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,-75,119,-83,-83,-83,-83,-83,-57,-68,-69,-72,-73,-78,]),'TO':([87,90,91,92,93,94,95,96,98,100,101,102,118,120,121,123,124,125,126,127,128,129,130,133,134,137,138,139,148,152,155,156,157,158,159,160,172,173,174,175,176,177,],[-79,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,-53,-55,-56,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,168,-75,-83,-83,-83,-83,-83,-83,-54,-57,-68,-69,-72,-73,]),'DO':([87,90,91,92,93,94,95,96,98,100,101,102,118,120,121,123,124,125,126,127,128,129,130,133,134,137,138,139,152,155,156,157,158,159,160,172,173,174,175,176,177,182,],[-79,-83,-83,-59,-60,-83,-83,-83,-78,-80,-81,-82,-53,-55,-56,-58,-61,-62,-63,-64,-65,-66,-67,-70,-71,-74,-76,-77,-75,-83,-83,-83,-83,-83,-83,-54,-57,-68,-69,-72,-73,187,]),'ELSE':([185,],[191,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'add_type':([2,],[3,]),'add_id':([4,],[5,]),'save_id':([6,],[7,]),'VARS_PRIME':([7,39,85,86,],[8,45,112,113,]),'VARS':([7,39,85,86,],[9,9,9,9,]),'empty':([7,8,13,23,28,39,40,41,43,45,54,68,85,86,89,90,91,94,95,96,106,107,112,113,115,149,155,156,157,158,159,160,163,164,166,167,185,193,194,],[10,14,25,25,36,10,48,48,36,55,55,84,10,10,117,120,123,129,133,137,144,144,55,55,117,84,120,123,133,133,137,137,144,144,55,55,192,55,55,]),'FUNCTION_PRIME':([8,],[12,]),'FUNCTION':([8,13,23,],[13,23,23,]),'TIPO_COMP':([11,],[16,]),'TIPO_SIMPLE':([11,15,40,41,83,],[17,26,46,46,111,]),'FUNC_PRIME':([13,23,],[24,31,]),'TIPO_PRIME':([28,43,],[34,50,]),'PARAM':([40,41,],[47,49,]),'BLOCK':([45,54,112,113,166,167,193,194,],[53,76,150,151,180,181,195,196,]),'STATEMENT':([45,54,112,113,166,167,193,194,],[54,54,54,54,54,54,54,54,]),'ASSIGNATION':([45,54,112,113,166,167,193,194,],[56,56,56,56,56,56,56,56,]),'FUNC_CALL':([45,54,112,113,166,167,193,194,],[57,57,57,57,57,57,57,57,]),'WRITE':([45,54,112,113,166,167,193,194,],[58,58,58,58,58,58,58,58,]),'CONDITION':([45,54,112,113,166,167,193,194,],[59,59,59,59,59,59,59,59,]),'WHILE_STMT':([45,54,112,113,166,167,193,194,],[60,60,60,60,60,60,60,60,]),'FOR_STMT':([45,54,112,113,166,167,193,194,],[61,61,61,61,61,61,61,61,]),'DESCRIBE_STMT':([45,54,112,113,166,167,193,194,],[62,62,62,62,62,62,62,62,]),'VARIABLE':([45,54,112,113,166,167,193,194,],[63,63,63,63,63,63,63,63,]),'PARAM_PRIME':([68,149,],[82,169,]),'EXPRESSION':([72,74,77,78,79,80,88,89,110,115,143,168,170,],[89,104,105,106,108,109,114,115,148,115,163,182,183,]),'AND_EXP':([72,74,77,78,79,80,88,89,110,115,119,143,168,170,],[90,90,90,90,90,90,90,90,90,90,155,90,90,90,]),'B_EXP':([72,74,77,78,79,80,88,89,110,115,119,122,143,168,170,],[91,91,91,91,91,91,91,91,91,91,91,156,91,91,91,]),'EXP':([72,74,77,78,79,80,88,89,110,115,119,122,143,168,170,],[94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,]),'TERM':([72,74,77,78,79,80,88,89,110,115,119,122,131,132,143,168,170,],[95,95,95,95,95,95,95,95,95,95,95,95,157,158,95,95,95,]),'FACTOR':([72,74,77,78,79,80,88,89,110,115,119,122,131,132,135,136,143,168,170,],[96,96,96,96,96,96,96,96,96,96,96,96,96,96,159,160,96,96,96,]),'VAR_CT':([72,74,77,78,79,80,88,89,97,99,110,115,119,122,131,132,135,136,143,168,170,],[98,98,98,98,98,98,98,98,138,139,98,98,98,98,98,98,98,98,98,98,184,]),'FUNC_CALL_PRIME':([89,115,],[116,153,]),'EXPRESSION_PRIME':([90,155,],[118,172,]),'AND_EXP_PRIME':([91,156,],[121,173,]),'B_EXP_PRIME':([94,],[124,]),'EXP_PRIME':([95,157,158,],[130,174,175,]),'TERM_PRIME':([96,159,160,],[134,176,177,]),'WRITE_PRIME':([106,107,163,164,],[142,145,178,179,]),'ELSE_STMT':([185,],[190,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> PROG add_type ID add_id ; save_id VARS_PRIME FUNCTION_PRIME VOID MAIN { VARS_PRIME BLOCK }','PROGRAM',14,'p_PROGRAM','parser.py',9),
  ('add_id -> <empty>','add_id',0,'p_add_id','parser.py',14),
  ('add_type -> <empty>','add_type',0,'p_add_type','parser.py',18),
  ('save_id -> <empty>','save_id',0,'p_save_id','parser.py',22),
  ('VARS_PRIME -> VARS','VARS_PRIME',1,'p_VARS_PRIME','parser.py',27),
  ('VARS_PRIME -> empty','VARS_PRIME',1,'p_VARS_PRIME','parser.py',28),
  ('FUNCTION_PRIME -> FUNCTION FUNC_PRIME','FUNCTION_PRIME',2,'p_FUNCTION_PRIME','parser.py',34),
  ('FUNCTION_PRIME -> empty','FUNCTION_PRIME',1,'p_FUNCTION_PRIME','parser.py',35),
  ('FUNC_PRIME -> FUNCTION FUNC_PRIME','FUNC_PRIME',2,'p_FUNC','parser.py',41),
  ('FUNC_PRIME -> empty','FUNC_PRIME',1,'p_FUNC','parser.py',42),
  ('VARS -> VAR TIPO_COMP ID TIPO_PRIME ;','VARS',5,'p_VARS','parser.py',48),
  ('VARS -> VAR TIPO_SIMPLE ID ;','VARS',4,'p_VARS','parser.py',49),
  ('VARS -> VAR TIPO_SIMPLE ID [ I_CONST ] ;','VARS',7,'p_VARS','parser.py',50),
  ('TIPO_PRIME -> , ID TIPO_PRIME','TIPO_PRIME',3,'p_TIPO_PRIME','parser.py',56),
  ('TIPO_PRIME -> empty','TIPO_PRIME',1,'p_TIPO_PRIME','parser.py',57),
  ('VARIABLE -> ID','VARIABLE',1,'p_VARIABLE','parser.py',63),
  ('VARIABLE -> ID [ EXPRESSION ]','VARIABLE',4,'p_VARIABLE','parser.py',64),
  ('TIPO_SIMPLE -> INT','TIPO_SIMPLE',1,'p_TIPO_SIMPLE','parser.py',70),
  ('TIPO_SIMPLE -> FLOAT','TIPO_SIMPLE',1,'p_TIPO_SIMPLE','parser.py',71),
  ('TIPO_SIMPLE -> CHAR','TIPO_SIMPLE',1,'p_TIPO_SIMPLE','parser.py',72),
  ('TIPO_COMP -> DATAFRAME','TIPO_COMP',1,'p_TIPO_COMP','parser.py',78),
  ('FUNCTION -> FUNC TIPO_SIMPLE ID ( PARAM ) { VARS_PRIME BLOCK RETURN EXPRESSION }','FUNCTION',12,'p_FUNCTION','parser.py',84),
  ('FUNCTION -> FUNC TIPO_SIMPLE ID ( PARAM ) { VARS_PRIME BLOCK RETURN VAR_CT }','FUNCTION',12,'p_FUNCTION','parser.py',85),
  ('FUNCTION -> FUNC VOID ID ( PARAM ) { VARS_PRIME BLOCK }','FUNCTION',10,'p_FUNCTION','parser.py',86),
  ('PARAM -> TIPO_SIMPLE ID PARAM_PRIME','PARAM',3,'p_PARAM','parser.py',92),
  ('PARAM -> empty','PARAM',1,'p_PARAM','parser.py',93),
  ('PARAM_PRIME -> , TIPO_SIMPLE ID PARAM_PRIME','PARAM_PRIME',4,'p_PARAM_PRIME','parser.py',99),
  ('PARAM_PRIME -> empty','PARAM_PRIME',1,'p_PARAM_PRIME','parser.py',100),
  ('BLOCK -> STATEMENT BLOCK','BLOCK',2,'p_BLOCK','parser.py',106),
  ('BLOCK -> empty','BLOCK',1,'p_BLOCK','parser.py',107),
  ('STATEMENT -> ASSIGNATION','STATEMENT',1,'p_STATEMENT','parser.py',113),
  ('STATEMENT -> FUNC_CALL','STATEMENT',1,'p_STATEMENT','parser.py',114),
  ('STATEMENT -> WRITE','STATEMENT',1,'p_STATEMENT','parser.py',115),
  ('STATEMENT -> CONDITION','STATEMENT',1,'p_STATEMENT','parser.py',116),
  ('STATEMENT -> WHILE_STMT','STATEMENT',1,'p_STATEMENT','parser.py',117),
  ('STATEMENT -> FOR_STMT','STATEMENT',1,'p_STATEMENT','parser.py',118),
  ('STATEMENT -> DESCRIBE_STMT','STATEMENT',1,'p_STATEMENT','parser.py',119),
  ('ASSIGNATION -> VARIABLE = EXPRESSION','ASSIGNATION',3,'p_ASSIGNATION','parser.py',125),
  ('FUNC_CALL -> ID ( EXPRESSION FUNC_CALL_PRIME )','FUNC_CALL',5,'p_FUNC_CALL','parser.py',131),
  ('FUNC_CALL_PRIME -> EXPRESSION FUNC_CALL_PRIME','FUNC_CALL_PRIME',2,'p_FUNC_CALL_PRIME','parser.py',137),
  ('FUNC_CALL_PRIME -> empty','FUNC_CALL_PRIME',1,'p_FUNC_CALL_PRIME','parser.py',138),
  ('WRITE -> PRINT ( EXPRESSION WRITE_PRIME )','WRITE',5,'p_WRITE','parser.py',144),
  ('WRITE -> PRINT ( TITLE WRITE_PRIME )','WRITE',5,'p_WRITE','parser.py',145),
  ('WRITE_PRIME -> , EXPRESSION WRITE_PRIME','WRITE_PRIME',3,'p_WRITE_PRIME','parser.py',151),
  ('WRITE_PRIME -> , TITLE WRITE_PRIME','WRITE_PRIME',3,'p_WRITE_PRIME','parser.py',152),
  ('WRITE_PRIME -> empty','WRITE_PRIME',1,'p_WRITE_PRIME','parser.py',153),
  ('CONDITION -> IF ( EXPRESSION ) { BLOCK } ELSE_STMT','CONDITION',8,'p_CONDITION','parser.py',159),
  ('ELSE_STMT -> ELSE { BLOCK }','ELSE_STMT',4,'p_ELSE_STMT','parser.py',165),
  ('ELSE_STMT -> empty','ELSE_STMT',1,'p_ELSE_STMT','parser.py',166),
  ('WHILE_STMT -> WHILE ( EXPRESSION ) { BLOCK }','WHILE_STMT',7,'p_WHILE_STMT','parser.py',172),
  ('FOR_STMT -> FOR ID = EXPRESSION TO EXPRESSION DO { BLOCK }','FOR_STMT',10,'p_FOR_STMT','parser.py',178),
  ('DESCRIBE_STMT -> ID . DESCRIBE ( )','DESCRIBE_STMT',5,'p_DESCRIBE_STMT','parser.py',184),
  ('EXPRESSION -> AND_EXP EXPRESSION_PRIME','EXPRESSION',2,'p_EXPRESSION','parser.py',190),
  ('EXPRESSION_PRIME -> OR AND_EXP EXPRESSION_PRIME','EXPRESSION_PRIME',3,'p_EXPRESSION_PRIME','parser.py',196),
  ('EXPRESSION_PRIME -> empty','EXPRESSION_PRIME',1,'p_EXPRESSION_PRIME','parser.py',197),
  ('AND_EXP -> B_EXP AND_EXP_PRIME','AND_EXP',2,'p_AND_EXP','parser.py',203),
  ('AND_EXP_PRIME -> AND B_EXP AND_EXP_PRIME','AND_EXP_PRIME',3,'p_AND_EXP_PRIME','parser.py',209),
  ('AND_EXP_PRIME -> empty','AND_EXP_PRIME',1,'p_AND_EXP_PRIME','parser.py',210),
  ('B_EXP -> TRUE','B_EXP',1,'p_B_EXP','parser.py',216),
  ('B_EXP -> FALSE','B_EXP',1,'p_B_EXP','parser.py',217),
  ('B_EXP -> EXP B_EXP_PRIME','B_EXP',2,'p_B_EXP','parser.py',218),
  ('B_EXP_PRIME -> >','B_EXP_PRIME',1,'p_B_EXP_PRIME','parser.py',224),
  ('B_EXP_PRIME -> <','B_EXP_PRIME',1,'p_B_EXP_PRIME','parser.py',225),
  ('B_EXP_PRIME -> DIFFERENT','B_EXP_PRIME',1,'p_B_EXP_PRIME','parser.py',226),
  ('B_EXP_PRIME -> EQUAL','B_EXP_PRIME',1,'p_B_EXP_PRIME','parser.py',227),
  ('B_EXP_PRIME -> empty','B_EXP_PRIME',1,'p_B_EXP_PRIME','parser.py',228),
  ('EXP -> TERM EXP_PRIME','EXP',2,'p_EXP','parser.py',234),
  ('EXP_PRIME -> + TERM EXP_PRIME','EXP_PRIME',3,'p_EXP_PRIME','parser.py',240),
  ('EXP_PRIME -> - TERM EXP_PRIME','EXP_PRIME',3,'p_EXP_PRIME','parser.py',241),
  ('EXP_PRIME -> empty','EXP_PRIME',1,'p_EXP_PRIME','parser.py',242),
  ('TERM -> FACTOR TERM_PRIME','TERM',2,'p_TERM','parser.py',248),
  ('TERM_PRIME -> * FACTOR TERM_PRIME','TERM_PRIME',3,'p_TERM_PRIME','parser.py',254),
  ('TERM_PRIME -> / FACTOR TERM_PRIME','TERM_PRIME',3,'p_TERM_PRIME','parser.py',255),
  ('TERM_PRIME -> empty','TERM_PRIME',1,'p_TERM_PRIME','parser.py',256),
  ('FACTOR -> ( EXPRESSION )','FACTOR',3,'p_FACTOR','parser.py',262),
  ('FACTOR -> * VAR_CT','FACTOR',2,'p_FACTOR','parser.py',263),
  ('FACTOR -> / VAR_CT','FACTOR',2,'p_FACTOR','parser.py',264),
  ('FACTOR -> VAR_CT','FACTOR',1,'p_FACTOR','parser.py',265),
  ('VAR_CT -> ID','VAR_CT',1,'p_VAR_CT','parser.py',271),
  ('VAR_CT -> I_CONST','VAR_CT',1,'p_VAR_CT','parser.py',272),
  ('VAR_CT -> F_CONST','VAR_CT',1,'p_VAR_CT','parser.py',273),
  ('VAR_CT -> C_CONST','VAR_CT',1,'p_VAR_CT','parser.py',274),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',283),
]
