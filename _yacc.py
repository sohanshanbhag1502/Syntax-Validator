from _lex import tokens
import ply.yacc as yacc

start='st'

def p_vartype(p):
	'''vartype : BYTE
	| SHORT
	| INT
	| LONG
	| DOUBLE
	| BOOLEAN
	| CHAR
	| STRING
	'''

def p_param(p):
	'''param : ID COLON vartype
	| param COMMA ID COLON vartype
	'''

def p_type(p):
	'''type : VAR 
	| VAL'''

def p_expression(p):
	'''expression : STR
	| CH
	| NUMBER
	| ID
	| TRUE
	| FALSE
	| ID EQUALS expression
	| expression NOTEQUALS expression 
	| expression LTHAN expression
	| expression GTHAN expression
	| expression GTE expression
	| expression LTE expression
	| expression EE expression
	| expression PLUS expression
	| expression MINUS expression
	| expression INTO expression
	| expression DIVIDE expression
	| expression MODULUS expression
	| expression AND expression
	| expression OR expression
	| expression INC
	| expression DEC
	| INC expression
	| DEC expression
	| NOT expression
	| LPAREN expression RPAREN
	| NUMBER POINT NUMBER
	'''

def p_nonstrdec(p):
	'''nonstrdec : type ID COLON BYTE EQUALS expression
	| type ID COLON SHORT EQUALS expression
	| type ID COLON INT EQUALS expression
	| type ID COLON LONG EQUALS expression
	| type ID COLON DOUBLE EQUALS expression
	| type ID COLON BOOLEAN expression
	'''

def p_strdec(p):
	'''strdec : type ID COLON CHAR EQUALS CH
	| type ID COLON STRING EQUALS STR
	'''

def p_variable_declaration(p):
	'''variable_declaration : type ID
	| type ID SEMICOLON
	| type ID EQUALS expression 
	| type ID EQUALS expression SEMICOLON
	| nonstrdec
	| strdec
	| nonstrdec SEMICOLON
	| strdec SEMICOLON
	'''
	print("valid variable declaration")

def p_whileloop(p):
	'''whileloop : WHILE LPAREN expression RPAREN LBRACE st RBRACE
	'''
	print('valid while loop')

def p_forloop(p):
	'''forloop : FOR LPAREN ID IN ID RPAREN LBRACE st RBRACE
	'''
	print('valid for loop')

def p_ifelse(p):
	'''ifelse : IF LPAREN expression RPAREN LBRACE st RBRACE ELSE LBRACE st RBRACE
	'''
	print('valid ifelse block')

def p_func(p):
	'''func : FUN ID LPAREN param RPAREN COLON vartype LBRACE st RBRACE
	| FUN ID LPAREN param RPAREN LBRACE st RBRACE
	'''
	print('valid function definition')

def p_rparams(p):
	''' rparams : rparams COMMA expression
	| expression
	|'''

def p_print(p):
	''' print : PRINTLN LPAREN rparams RPAREN
	'''

def p_st(p):
	'''st : variable_declaration
	| whileloop
	| forloop
	| ifelse
	| func
	| expression
	| print
	|'''

def p_error(p):
	if p:
		print(f"syntax error at line {p.lineno}: Unexpected token \'{p.value}\'")
	else:
		print(f"syntax error : Unexpected EOF")

parser=yacc.yacc()

while True:
	try:
		s=input(">>> ")
	except EOFError:
		break
	if not s:
		continue
	parser.parse(s)