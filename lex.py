import ply.lex as lex
import ply.yacc as yacc

keywords={'val':'VAL','var':'VAR','while':'WHILE','for':'FOR', 'if':'IF', 
		'else':'ELSE', 'fun':'FUN', 'in':'IN', 'Byte':'BYTE', 'Short':'SHORT', 'Int':'INT',
		'Long':'LONG', 'Double':'DOUBLE', 'Boolean':'BOOLEAN', 'Char':'CHAR', 'String':'STRING',
		'as':'AS', 'break':'BREAK', 'class':'CLASS', 'continue':'CONTINUE', 'do':'DO', 
		'interface':'INTERFACE', 'is':'IS', 'null':'NULL', 'object':'OBJECT', 
		'package':'PACKAGE', 'return':'RETURN', 'super':'SUPER', 'this':'THIS', 
		'throw':'THROW', 'true':'TRUE', 'false':'FALSE', 'try':'TRY', 'typealias':'TYPEALIAS', 
		'typeof':'TYPEOF', 'when':'WHEN',
		'println':'PRINTLN'}
tokens=(
	'LPAREN',
	'RPAREN',
	'NOT',
	'EE',
	'NOTEQUALS',
	'SEMICOLON',
	'LTHAN',
	'GTHAN',
	'GTE',
	'LTE',
	'INC',
	'DEC',
	'AND',
	'OR',
	'EQUALS',
	'ID',
	'NUMBER',
	'PLUS',
	'MINUS',
	'INTO',
	'DIVIDE',
	'MODULUS',
	'LBRACE',
	'RBRACE',
	'COLON',
	'COMMA',
	'QUOTE',
	'DQUOTE',
	'POINT',
	'STR',
	'ID1',
	'CH'
)+tuple(keywords.values())

t_LPAREN=r'\('
t_RPAREN=r'\)'
t_NOT=r'\!'
t_EE=r'=='
t_NOTEQUALS=r'\!='
t_EQUALS=r'='
t_SEMICOLON=r';'
t_LTHAN=r'\<'
t_GTHAN=r'\>'
t_GTE=r'\>='
t_LTE=r'\<='
t_PLUS=r'\+'
t_INC=r'\+{2}'
t_DEC=r'\-{2}'
t_AND=r'\&{2}'
t_OR=r'\|\|'
t_MINUS=r'\-'
t_INTO=r'\*'
t_DIVIDE=r'/'
t_MODULUS=r'%'
t_LBRACE=r'\{'
t_RBRACE=r'\}'
t_COLON=r'\:'
t_COMMA=r'\,'
t_QUOTE=r'\''
t_DQUOTE=r'\"'
t_POINT=r'\.'

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type=keywords.get(t.value,'ID')
	return t

def t_NUMBER(t):
	r'\d+'
	t.value=int(t.value)
	return t

def t_STR(t):
    r'(\"[^\"]*\")'
    return t

def t_CH(t):
	r'(\'[^\n]\')'
	return t

t_ignore=' \t'

def t_error(t):
	print(f"Illegal character'{t.value[0]}'")
	t.lexer.skip(1)

lexer=lex.lex()
