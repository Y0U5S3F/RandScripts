%option noyywrap
%{
#include <stdio.h>
int num_lines = 1;
%}

%%

\n      { ++num_lines; }
.|\n    { /* Ignore all other characters */ }

%%

int main(void) {
    yylex();
    printf("number of lines is : %d\n", num_lines);
    return 0;
}