%{
int yylex(void); /* -Wall : avoid implicit call */
int yyerror(const char*); /* same for bison */
%}

%token NOMBRE
%start resultat /* axiom */

%% 

resultat: expression
;

expression:
    expression '+' expression
    | expression '-' expression
    | expression '*' expression
    | expression '/' expression
    | '(' expression ')'
    | '-' expression
    | NOMBRE /* default semantic value */
;

%%

#include <stdio.h> /* printf */

int yyerror(const char *msg) { 
    printf("Parsing:: syntax error\n"); 
    return 1;
}

int yywrap(void) { 
    return 1; 
} /* stop reading flux yyin */