#include <stdio.h> /* printf */
#include <stdlib.h> /* exit */

int yyparse(void); /* prototype of yyparse */

int main(void)
{
    if (yyparse() == 0) { /* yyparse calls yylex */
        printf("\nParsing:: syntax OK\n"); /* reached if parsing follows the grammar*/
    }
    exit(EXIT_SUCCESS);
}