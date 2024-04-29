%option noyywrap
%{
#include <stdio.h>
%}

%%

[a-zA-Z_][a-zA-Z0-9_]*    { printf("Identificateur C: %s\n", yytext); }
'([^']|'')*'              { printf("Chaine de caractères Pascal: %s\n", yytext); }
\"(\\.|[^"\\])*\"         { printf("Chaine de caractères C: %s\n", yytext); }
\/\/.*                    { printf("Commentaire C++: %s\n", yytext); }
0[xX][0-9a-fA-F]+         { printf("Entier hexadécimal: %s\n", yytext); }
0[0-7]*                   { printf("Entier octal: %s\n", yytext); }
[1-9][0-9]*               { printf("Entier décimal: %s\n", yytext); }
[0-9]*\.[0-9]+([eE][-+]?[0-9]+)? { printf("Réel avec exposant: %s\n", yytext); }
.                          { printf("Caractère non reconnu: %s\n", yytext); }

%%

int main() {
    yylex();
    return 0;
}