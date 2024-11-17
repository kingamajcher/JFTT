/* Kinga Majcher 272354 */

%{
#include <stdio.h>

int yywrap();
int yylex();

int linesCount = 0;
int wordsCount = 0;
%}

%%
^[[:blank:]]*\n
[[:blank:]]+         { printf(" "); }
[^ \t\n]+            { printf("%s", yytext); wordsCount++; }
\n                   { printf("\n"); linesCount++; }
%%

int yywrap() {
    printf("\nLines: %d\nWords: %d\n", linesCount, wordsCount);
    return 1;
}

int main() {
    return yylex();
}
