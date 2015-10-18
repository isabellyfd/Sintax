# lexer

import ply.lex as lex

tokens = (
	'COMMENT',
	'WHITESPACE',
	'DELIMITER',
	'OP',
	'KEYWORD',
	'IDENTIFIER',
	'FT',
	'INTEGER',
	)



digit = r'([0-9])'
letter = r'([A-za-z])'


def t_COMMENT(t):
	r'/\*~\*/'
	pass

def t_WHITESPACE(t):
	r'([\n\t ])'
	pass


def t_DELIMITER(t):
	r'([;.=(){}[]])'
	return "TOKEN: " + t

def t_OP(t):
	r'(&&|==|!=|<|<=|>=|-|%|\|\||\+|\*|/|!)'
	return "TOKEN: " + t	

def t_KEYWORD(t):
	r'(class|public|int|static|void|boolean|while|if|else|return|false|true|this|new)'
	return "TOKEN: " + t

def t_IDENTIFIER(t):
	r'((_' r'|' + letter + r')' + r'((' + letter + r')*' + r'|' + r'(' + digit + r')*' + r'|' + r'(' + integer + r')*))' 
	return "TOKEN :" + t

def t_FT(t):
	r'(' + integer + r'.' + r'(' + digit + r')+)'
	return "TOKEN :" + t

def t_INTEGER(t):
	r'(([1-9]' + r'(' + digit + r')*)' r'|' + r'0' + r')'
	return "TOKEN :" + t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
#build lexer
 lexer = lex.lex()
 #put the input
 lexer.input('/src/quicksort.java')

 #tokenize
 while True:
 	tok = lexer.token()
 	if not tok:
 		break
 	print(tok)

