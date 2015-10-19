
###LEXER###

reserved = {
		'System':'SYSTEM',
		'class':'CLASS',
		'String' :'STRING',
		'public':'PUBLIC',
		'extends':'EXTENDS',
		'static': 'STATIC',
		'void':'VOID',
		'main':'MAIN',
		'int': 'INT',
		'boolean': 'BOOLEAN',
		'while':'WHILE',
		'if':'IF',
		'else':'ELSE',
		'return':'RETURN',
		'false':'FALSE',
		'true': 'TRUE',
		'this':'THIS',
		'new':'NEW'
	}


_tokens = [
	'SYSTEM_PRINTLN',
	'LENGTH',
	'WHITESPACE'
	'COMMENT',
	'DELIMITER',
	'OP',
	'FT',
	'IDENTIFIER',
	'INTEGER',
	'AND',
	'LESSTHAN',
	'NOT',
	'PLUS',
	'MINUS',
	'TIMES',
	'LPAREN',
	'RPAREN',
	'LBRACE',
	'RBRACE',
	'LBRACKET',
	'RBRACKET',
	'SEMICOLON',
	'DOT',
	'COMMA',
	'ATTR', 
	] + list(reserved.values())

tokens = tuple(_tokens)

t_CLASS = r'class'
t_PUBLIC = r'public'
t_STATIC = r'static'
t_VOID = r'void'
t_MAIN = r'main'
t_STRING = r'String'
t_EXTENDS = r'extends'
t_RETURN = r'return'
t_INT = r'int'
t_BOOLEAN = r'boolean'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_ATTR = r'='
t_AND = r'&&'
t_LESSTHAN = r'<'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_TRUE = r'true'
t_FALSE = r'false'
t_THIS = r'this'
t_NEW = r'new'
t_NOT = r'!'
t_COMMA = r','
t_DOT = r'\.'
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

def t_COMMENT(t):
	r'(/\*.*\*/)|(//.*)'
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

##def t_KEYWORD(t):
##	r'(class|public|int|static|void|boolean|while|if|else|return|false|true|this|new)'
##	return t

def t_IDENTIFIER(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*' 
	return t

def t_FT(t):
	r'((([1-9][0-9]*)|0).[0-9]+)'
	return t

def t_INTEGER(t):
	r'(([1-9][0-9]*)|0)'
	t.value = int(t.value)
	return t

def t_SYSTEM_PRINTLN(t):
	r'System\.out\.println'
	return t
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


### PARSER ###

## GRAMMAR RULES
#Goal	::=	MainClass ( ClassDeclaration )* <EOF>

## _declaration significa que tem 0 ou mais vezes
def p_goal(p):
	'''goal : mainclass declaration_star''' 
	print("GOAL")

## ClassDeclaration	::=	"class" Identifier ( "extends" Identifier )? "{" ( VarDeclaration )* ( MethodDeclaration )* "}"
def p_classdeclaration(p):
	'''classdeclaration : CLASS identifier  optional_extends LBRACE classbody RBRACE'''
	print("CLASS DECLARATION")

def p_classbody(p):
	'''classbody : vardeclaration_star
					| methoddeclaration_star
					| vardeclaration_star methoddeclaration_star'''

## MANY DECLARATIONS OF CLASS DECLARATON OR NONE
def p_declaration_star(p):
	'''declaration_star : classdeclaration declaration_star 
						| empty'''
	print("PLUS CLASSES DECLARATION")

##MainClass	::=	"class" Identifier "{" "public" "static" "void" "main" "(" "String" "[" "]" Identifier ")" "{" Statement "}" "}"
def p_mainclass(p):
	'''mainclass : CLASS identifier LBRACE PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET identifier RPAREN LBRACE statement RBRACE RBRACE'''
	print("MAIN CLASS")

def p_optional_extends(p):
	'''optional_extends : EXTENDS identifier 
						| empty'''
	print("CLASS EXTENDS...")

## VarDeclaration ::= Type Identifier ";"
def p_vardeclaration(p):
	'''vardeclaration : type identifier SEMICOLON'''
	print("VAR DECLARATION")

## MANY DECLARATIONS OF VARS OR NONE
def p_vardeclaration_star(p):
	'''vardeclaration_star : vardeclaration vardeclaration_star 
						   | empty'''
	print("MANY VAR DECLARATIONS") 

## MethodDeclaration	::=	"public" Type Identifier "(" ( Type Identifier ( "," Type Identifier )* )? ")" "{" ( VarDeclaration )* ( Statement )* "return" Expression ";" "}"
def p_methoddeclaration(p):
	'''methoddeclaration : PUBLIC type identifier LPAREN  type identifier argument_star_opt  RPAREN LBRACE methodbody RETURN exp SEMICOLON RBRACE'''
	print('METHOD DECLARATION')

def p_methodbody(p):
	'''methodbody : statement_star
				  | vardeclaration_star
				  | vardeclaration_star statement_star'''

def p_methoddeclaration_star(p):
	'''methoddeclaration_star : methoddeclaration methoddeclaration_star 
							  | empty'''
	print("MANY VAR DECLARATION")

##Type	::=	"int" "[" "]"
##	|	"boolean"
##	|	"int"
##	|	Identifier

def p_type(p):
	'''type : INT LBRACKET RBRACKET
			| BOOLEAN
			| INT
			| identifier'''
	print("TYPE")

## MANY ARGUMENTS OR NONE | OPTIONAL
def p_argument_star_opt(p):
	'''argument_star_opt : COMMA type identifier
						 | empty'''
	print("MANY ARGUMENTS")

##Statement	::=	"{" ( Statement )* "}"
##	|	"if" "(" Expression ")" Statement "else" Statement
##	|	"while" "(" Expression ")" Statement
##	|	"System.out.println" "(" Expression ")" ";"
##	|	Identifier "=" Expression ";"
##	|	Identifier "[" Expression "]" "=" Expression ";"

def p_statement(p):
	'''statement : LBRACE statement_star RBRACE
				 | IF LPAREN exp RPAREN statement ELSE statement
				 | WHILE LPAREN exp RPAREN statement
				 | SYSTEM_PRINTLN LPAREN exp RPAREN SEMICOLON
				 | identifier ATTR exp SEMICOLON
				 | identifier LBRACKET exp RBRACKET ATTR exp SEMICOLON'''
	print("STATEMENT")

## MANY OR NONE STATEMENTS
def p_statement_star(p):
	'''statement_star : statement statement_star
					  | empty'''
	print("MANY STATEMENTS")

##Expression	::=	Expression ( "&&" | "<" | "+" | "-" | "*" ) Expression
##	|	Expression "[" Expression "]"
##	|	Expression "." "length"
##	|	Expression "." Identifier "(" ( Expression ( "," Expression )* )? ")"
##	|	<INTEGER_LITERAL>
##	|	"true"
##	|	"false"
##	|	Identifier
##	|	"this"
##	|	"new" "int" "[" Expression "]"
##	|	"new" Identifier "(" ")"
##	|	"!" Expression
##	|	"(" Expression ")"

def p_exp(p):
	'''exp : exp AND exp
		   | exp LESSTHAN exp
		   | exp PLUS exp
		   | exp MINUS exp
	       | exp TIMES exp
		   | exp LBRACKET exp RBRACKET
		   | exp DOT LENGTH
		   | exp DOT identifier LPAREN exp opt_exp RPAREN
		   | INTEGER
		   | TRUE
		   | FALSE
		   | identifier
		   | THIS
		   | NEW INT LBRACKET exp RBRACKET
		   | NEW identifier LPAREN RPAREN
		   | NOT exp
		   | LPAREN exp RPAREN'''
	print("EXPRESSION")

def p_opt_exp(p):
	'''opt_exp : COMMA exp opt_exp
			   | empty'''
	print("MANY EXPRESSIONS")

def p_identifier(p): 
	'''identifier : IDENTIFIER'''
	print("IDENTIFIER")

def p_error(p):
	print("SINTAX ERROR")

def p_empty(p):
	'''empty :'''
	pass

import ply.lex as lex
import ply.yacc as yacc

#BUILD LEXER
lexer = lex.lex()
#BUILD PARSER
yacc.yacc()
#INPUT
target = open('/home/isabelly/Documentos/git/Sintax/Compiler/src/factorial.java', 'r')
print "Target", target
in_file = target.read()
print("Data "), in_file
lexer.input(in_file)
while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)
yacc.parse(in_file) # DO THE PARSING