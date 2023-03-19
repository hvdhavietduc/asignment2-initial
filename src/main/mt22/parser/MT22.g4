//2012987
// Hà Việt Đức
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: parsercall_list EOF ;
parsercall_list: parsercall parsercall_list| parsercall;
parsercall:( vardecl 
            |funcdecl
           )
            ;



//----------------------------------------------------------------------------------------------------------------Array-----------
funcType: Inttype | Floattype | Stringtype | Booleantype| Voidtype | Autotype | arraytypeof;
typearray: Inttype | Floattype | Stringtype | Booleantype ;
array_expr : LCB (expression_BT_list|) RCB;
arraytypeof: Arraytype LSB intlist RSB Ofkey typearray ;
intlist: Int COMMA intlist| Int;
//----------------------------------------------------------------------------------------------------------------Khai bao danh sach bien------------------
idlist: Identifiers COMMA idlist |Identifiers ;

expression_list : expression_BT| expression_BT COMMA expression_list;
// ------------------------------------------------------------------------------------------------------------Danh sach bien------------------
// val_decl: listID COLON (TYPE|arr_decl) SEMI	| var_init;
// var_init: ID (COMMA recursive_decl|COLON (TYPE|arr_decl) ASSIGN) expr SEMI;
// recursive_decl: ID (COMMA recursive_decl|COLON (TYPE|arr_decl) ASSIGN) expr COMMA;
// arr_decl: ARRAY LSB listInt RSB OF ELE_TYPE;
vardecl: idlist COLON (typein| arraytypeof) SEMI | varinit  ;   
varinit: Identifiers (COMMA re_vardecl | COLON (typein|arraytypeof) ASS) (expression_BT) SEMI;
re_vardecl: Identifiers (COMMA re_vardecl | COLON (typein| arraytypeof) ASS ) (expression_BT) COMMA;




parameters: Inheritkey? Outkey? Identifiers COLON (typein|arraytypeof) ; // -------------------------------------------------------Parameters----------------------
parameters_list: parameters COMMA parameters_list| parameters;

//----------------------------------------------------------------------------------------------------------------Khai bao function------------
funcdecl: Identifiers COLON Functionkey funcType LB  parameters_list?  RB  (Inheritkey Identifiers)? blockstatement ;
//----------------------------------------------------------------------------------------------------------------Index Array----------
indexopr: Identifiers LSB expression_list RSB;
//----------------------------------------------------------------------------------------------------------------Goi function----------
callfunc: special_function| Identifiers  LB expression_list?  RB ;
//--------------------------------------------------------------------------------------------------------------------expression_BT-------


expression_BT: stringoprExpr  ;

//------------

//-----------

stringoprExpr: equalityExpr (Stringopr) equalityExpr| equalityExpr;
equalityExpr
    :  logicalExpr(EQUAL | NOT_EQUAL|GT | LT | GTE | LTE) logicalExpr
    | logicalExpr
    ;
logicalExpr
    :  logicalExpr(LOGICAL_AND|LOGICAL_OR) addExpr
    | addExpr
    ;
addExpr
    :   addExpr(PLUS | MINUS) multExpr 
    | multExpr
    ;
multExpr
    :   multExpr(MULT| DIV | MOD) unaryExpr 
    | unaryExpr
    ;
unaryExpr
    : MINUS unaryExpr
    | NOT unaryExpr
    | atom
    ;
atom
    : Identifiers
    | FLOAT
    | Identifiers LSB expression_BT RSB
    | indexopr
    | Int
    | callfunc 
    | booleann
    | String
    | LB expression_BT RB
    | array_expr
    ;


expression_BT_list: expression_BT| expression_BT COMMA expression_BT_list;

//--------------------------------------------------------------------------------------------------Statement-------------------

allstatement: assignment
            |if_statement
            |for_statement
            |while_statements
            |do_while_statements
            |break_stt
            |continue_stt
            |retunr_stt
            |call_stt
            |blockstatement
            ;



//--------------------------------------------------------------------------------------------------Gán-------------------
assignment: (Identifiers |indexopr) ASS (expression_BT) SEMI;


//--------------------------------------------------------------------------------------------------If else------------
if_statement: Ifkey LB expression_BT RB  allstatement (Else allstatement)?;

//---------------------------------------------------------------------------------------------------For-------------
for_statement: Forkey LB  assignment_offor COMMA expression_BT COMMA expression_BT  RB  allstatement;
assignment_offor:  (Identifiers |indexopr) ASS expression_BT;

//--------------------------------------------------------------------------------------------------while statement---------
while_statements: Whilekey  LB  expression_BT  RB  allstatement;

//--------------------------------------------------------------------------------------------------do-while statement---------
do_while_statements: Dokey blockstatement Whilekey  LB expression_BT  RB  SEMI;

//--------------------------------------------------------------------------------------------------break statement---------
break_stt: Breakkey SEMI;

//--------------------------------------------------------------------------------------------------continue statement---------
continue_stt: Continuekey SEMI;

//--------------------------------------------------------------------------------------------------return statement---------
retunr_stt: Returnkey (expression_BT)? SEMI;

//--------------------------------------------------------------------------------------------------call statement---------
call_stt: callfunc SEMI| Identifiers  LB  expression_BT_list?  RB  SEMI;

//--------------------------------------------------------------------------------------------------Block statement---------
blockstatement: 
    LCB
    block_allstatement?
    RCB
    ;
block_allstatement: blockstt block_allstatement| blockstt;
blockstt: 
        assignment
        |if_statement
        |for_statement
        |while_statements
        |do_while_statements
        |break_stt
        |continue_stt
        |retunr_stt
        |call_stt
        |vardecl
        |allstatement
;

//----------------------------------------------------------------Special function------------------

special_function:
    readInt_function
    | printInteger_function
    | readFloat_function
    | writeFloat_function
    | readBoolean_function
    | printBoolean_function
    | readString_function
    | printString_function
    | super_function
    | preventDefault
    ;
readInt_function: 'readInteger' LB RB;
printInteger_function: 'printInteger' LB expression_BT RB;
readFloat_function: 'readFloat' LB RB;
writeFloat_function: 'writeFloat' LB expression_BT RB;
readBoolean_function: 'readBoolean' LB RB;
printBoolean_function: 'printBoolean' LB expression_BT RB;
readString_function: 'readString' LB RB;
printString_function: 'printString' LB expression_BT RB;
super_function: 'super' LB expression_BT_list RB;
preventDefault: 'preventDefault' LB RB;


// Lexxer
Comment: ('/*' .*? '*/')  ->skip;
LineCmt: ('//' ~[\r\n]*) ->skip;
typein: Inttype | Floattype | Stringtype | Booleantype| Autotype ;
Inttype: 'integer';
Floattype: 'float';
Stringtype: 'string';
Booleantype: 'boolean';
Autotype: 'auto';
Breakkey: 'break';
Dokey:'do';
Else: 'else';
Trueboolean: 'true';
Falseboolean: 'false';
Functionkey: 'function';
Forkey: 'for';
Ifkey: 'if';
Returnkey: 'return';
Whilekey: 'while';
Voidtype: 'void';
Outkey: 'out';
Continuekey: 'continue';
Arraytype: 'array';
Inheritkey: 'inherit';
Ofkey: 'of';
booleann: Trueboolean|Falseboolean;
// Keyword: 'auto'| 'break' | 'boolean' | 'do' | 'else'
// | 'false' | 'float' | 'for' | 'function' | 'if' 
// | 'integer' | 'return' | 'string' | 'true' | 'while'
// | 'void' | 'out' | 'continue'  | 'of' | 'inherit'
// | 'array' ;
//-----------------------------------------------------------------------------------------------------Bien va ten bien va kieu du lieu---------------

Identifiers: [a-zA-Z_] [a-zA-Z0-9_]*;

Int: '0' | [1-9] ('_'? [0-9])* {self.text = self.text.replace("_","")};
Boolean: Trueboolean|Falseboolean;

String: '"' (Escape_sequence | ~[\n\\"] )* '"' {self.text = self.text[1:-1]};
fragment Escape_sequence: '\\' ['"\\bfnrt];


FLOAT
    :   INTEGER_PART DECIMAL_PART  {self.text = self.text.replace("_","")}
    |   INTEGER_PART DECIMAL_PART? EXPONENT_PART {self.text = self.text.replace("_","")}
    | DECIMAL_PART EXPONENT_PART
    ;
fragment INTEGER_PART:   '0'| [1-9] ('_'? [0-9])*  ;
fragment DECIMAL_PART:   '.'[0-9]*;
fragment EXPONENT_PART:   [eE] [+-]? [0-9]+;

LB:'(';
RB:')';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON : ':';
LCB:'{';
RCB: '}';
LSB: '[';
RSB:']';
ASS: '=';
PLUS: '+';
MULT: '*';
DIV: '/';
MOD: '%';
NOT: '!';
MINUS: '-';
EQUAL: '==';
NOT_EQUAL: '!=';
GT: '>';
LT: '<';
GTE: '>=';
LTE: '<=';
LOGICAL_AND: '&&';
LOGICAL_OR: '||';
Stringopr: '::';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines



UNCLOSE_STRING: 
'"' (~[\n\\"] | Escape_sequence )* (EOF | '\n') {
	text = self.text[1:-1] if self.text[-1] == '\n' else self.text[1:]
	raise UncloseString(text)

};
ILLEGAL_ESCAPE: 
'"' (~[\n\\"] | Escape_sequence )* '\\' ~[bntrf\\'"] {
	raise IllegalEscape(str(self.text[1:]))
};
ERROR_CHAR: . {raise ErrorToken(self.text)};