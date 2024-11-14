/* Kinga Majcher 272354 */

%{
#include <stdio.h>

int yywrap();
int yylex();

int linesCount = 0;
int wordsCount = 0;
%}

%%
^[[:blank:]]*\n 						/*usuwanie pustych linii*/
[[:blank:]]+         { printf(" "); }				/*zastępowanie ciągu białych znaków pojedynczą spacją*/
[^ \t\n]+            { printf("%s", yytext); wordsCount++; }	/*wypisywanie słowa i zwiększenie licznika słów*/
\n                   { printf("\n"); linesCount++; }		/*wypisywanie nowej linii i zwiększenie licznika linii*/
%%

int yywrap() {
    printf("\nLines: %d\nWords: %d\n", linesCount, wordsCount);
    return 1;
}

int main() {
    return yylex();
}
