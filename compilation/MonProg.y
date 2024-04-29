%{
#include <stdio.h>
extern int yylex();
void yyerror(char *s);
%}

/* Declare symbols */
%token NUMBER
%left '+' '-'
%left '*' '/'

%%

input: /* empty */
    | input line
    ;

line: '\n'
    | exp '\n' { printf("%d\n", $1); }
    ;

exp: NUMBER
    | exp '+' exp { $$ = $1 + $3; }
    | exp '-' exp { $$ = $1 - $3; }
    | exp '*' exp { $$ = $1 * $3; }
    | exp '/' exp { $$ = $1 / $3; }
    | '(' exp ')' { $$ = $2; }
    ;

%%

void yyerror(char *s) {
    fprintf(stderr, "error: %s\n", s);
}

