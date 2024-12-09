/* Kinga Majcher 272354 */

%{
#include <stdio.h>
int yywrap();
%}

%x COMMENT

%%

\"[^"\n]*\" 			{ ECHO; }


^[[:blank:]]*--.*\n     ; 
(^|[[:space:]]?)--      { BEGIN(COMMENT); }

<COMMENT>[^\n]*         ;
<COMMENT>\n             { BEGIN(INITIAL); ECHO; }

%%

int yywrap() {
    return 1;
}

int main() {
    return yylex();
}
