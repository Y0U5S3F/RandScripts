%{
#include <stdio.h> /* printf */
#include "parseur.tab.h" /* token constants def. in parseur.y via #define */
%}

%%

[0-9]+ { printf("lex::NOMBRE %s\n",yytext); return NOMBRE; }
[ \t\n] { ; } /* ignore space, tab, and line return */
. { printf("lex::char %s\n",yytext); return yytext[0]; }

%% 