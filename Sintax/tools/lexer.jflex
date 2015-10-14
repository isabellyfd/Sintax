package generate;

import java_cup.runtime.ComplexSymbolFactory;
import java_cup.runtime.ComplexSymbolFactory.Location;
import java_cup.runtime.Symbol;
import java.lang.*;
import java.io.InputStreamReader;

%%

%line
%column
%unicode
%public 
%class Lexer
%implements sym
%cup

%{
	

    public Lexer(ComplexSymbolFactory sf, java.io.InputStream is){
		this(is);
        symbolFactory = sf;
    }
	public Lexer(ComplexSymbolFactory sf, java.io.Reader reader){
		this(reader);
        symbolFactory = sf;
    }
    
    private StringBuffer sb;
    private ComplexSymbolFactory symbolFactory;
    private int csline,cscolumn;

    public Symbol symbol(String name, int code){
		return symbolFactory.newSymbol(name, code,
						new Location(yyline+1,yycolumn+1, yychar), // -yylength()
						new Location(yyline+1,yycolumn+yylength(), yychar+yylength())
				);
    }
    public Symbol symbol(String name, int code, String lexem){
	return symbolFactory.newSymbol(name, code, 
						new Location(yyline+1, yycolumn +1, yychar), 
						new Location(yyline+1,yycolumn+yylength(), yychar+yylength()), lexem);
    }
    
    protected void emit_warning(String message){
    	System.out.println("scanner warning: " + message + " at : 2 "+ 
    			(yyline+1) + " " + (yycolumn+1) + " " + yychar);
    }
    
    protected void emit_error(String message){
    	System.out.println("scanner error: " + message + " at : 2" + 
    			(yyline+1) + " " + (yycolumn+1) + " " + yychar);
    }
%}

%eofval{
    return symbolFactory.newSymbol("EOF",sym.EOF);
%eofval}

whitespace = [\n\t ]
comment = "/*"~"*/"
digit = [0-9]
integer = [1-9]{digit}* | 0
float = {integer}.{digit}+
letter = [A-z]|[a-z]
underline = _
identifier = ( {underline} | {letter} )( {letter}* | {integer}* | {digit}* )

%%
<YYINITIAL>{
";"|
"."|
"="|
"("|
")"|
"{"|
"}"|
"["|
"]" 
{ return symbolFactory.newSymbol("DEL", DEL); }
"&&"|
"=="|
"!="|
"<"|
"<="|
">="|
"-"|
"%"| 
"||"|
"+" |
"*" |
"/" |
 "!"
 { return symbolFactory.newSymbol("OP", OP); }
"class"|
"public"|
"int"|
"static"|
"void"|
"boolean"|
"while"|
"if"|
"else"|
"return"|
"false"|
"true"|
"this"|
"new"
{ return symbolFactory.newSymbol("KEYW", KEYW); }
{identifier}					{return symbolFactory.newSymbol("ID", ID); }
{float}							{return symbolFactory.newSymbol("FLOAT", FLOAT); }
{integer} 						{return symbolFactory.newSymbol("INTEGER", INTEGER); }
{whitespace}|{comment}   		{ /* Ignore */ }
}

. | \n			                { emit_error("Unrecognized character '" +yytext()+"' -- ignored"); }