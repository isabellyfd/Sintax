# -*- coding: utf-8 -*-

#### LEXER ####

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


def t_COMMENT(t):
	r'/\*~\*/|(//.*)'
	pass

def t_WHITESPACE(t):
	r'([\n\t ])'
	pass


def t_DELIMITER(t):
	r'(;|\.|=|\(|\)|\{|\}|\[|\])'
	return t

def t_OP(t):
	r'(&&|==|!=|<|<=|>=|-|%|\|\||\+|\*|/|!)'
	return t	

def t_KEYWORD(t):
	r'(class|public|int|static|void|boolean|while|if|else|return|false|true|this|new)'
	return t

def t_IDENTIFIER(t):
	r'((_|[A-za-z])(([A-za-z])*|[0-9]*|((([1-9][0-9]*)|0))*))' 
	return t

def t_FT(t):
	r'((([1-9][0-9]*)|0).[0-9]+)'
	return t

def t_INTEGER(t):
	r'(([1-9][0-9]*)|0)'
	return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
#build lexer
import ply.lex as lex

lexer = lex.lex()
print ("Lexer criado")
#put the input
target = open('/home/isabelly/Documentos/git/Sintax/Compiler/src/linkedlist.java', 'r')
print "Target", target
in_file = target.read()
print "Data ", in_file
print("Passando data pra o lexer")
lexer.input(in_file)
print ("Antes do while")
while True:
	print("Enntrou no while")
	tok = lexer.token()
	if not tok:
 		break
 	print(tok)

