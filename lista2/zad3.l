/* Kinga Majcher 272354*/

%{
    #include <stdio.h>
    #include <fcntl.h>
    int yylex();
    int yywrap();

    int docs = 0;
%} 

%x SINGLE_LINE_COMMENT
%x MULTI_LINE_COMMENT
%x SINGLE_LINE_DOCS_COMMENT
%x MULTI_LINE_DOCS_COMMENT
%x STRING
%x INCLUDE

%%
	
\"                       	                { ECHO; BEGIN(STRING); }
<STRING>\"   	                                { ECHO; BEGIN(INITIAL); }
<STRING>.           	                        { ECHO; }

"#include"                 	                { ECHO; BEGIN(INCLUDE); }
<INCLUDE>\"                                     { ECHO; BEGIN(STRING); }
<INCLUDE>\>                                     { ECHO; BEGIN(INITIAL); }


^[[:blank:]]*"//"                               { BEGIN(SINGLE_LINE_COMMENT); }
[[:blank:]]*"//"                                { BEGIN(SINGLE_LINE_COMMENT);  printf("\n");}
<SINGLE_LINE_COMMENT>[^\n]*\\\n                 ;
<SINGLE_LINE_COMMENT>[^\n]*                     ;
<SINGLE_LINE_COMMENT>\n                         { BEGIN(INITIAL); }

"/*"                                            { BEGIN(MULTI_LINE_COMMENT); }
<MULTI_LINE_COMMENT>[^\*]*                      ;
<MULTI_LINE_COMMENT>\*+[^/]                     ;
<MULTI_LINE_COMMENT>"*/"                        { BEGIN(INITIAL); }

"///"|"//!"                                     { if(docs) ECHO;BEGIN(SINGLE_LINE_DOCS_COMMENT); }
<SINGLE_LINE_DOCS_COMMENT>[^\\\n]*\\\n          { if(docs) ECHO; }
<SINGLE_LINE_DOCS_COMMENT>[^\n]*                { if(docs) ECHO; }
<SINGLE_LINE_DOCS_COMMENT>\n                    { if(docs) ECHO;BEGIN(INITIAL); } 

"/**"|"/*!"                  	                { if(docs) ECHO; BEGIN(MULTI_LINE_DOCS_COMMENT); }
<MULTI_LINE_DOCS_COMMENT>[^\*]*        	        { if(docs) ECHO; }
<MULTI_LINE_DOCS_COMMENT>\*+[^/]                { if(docs) ECHO; }
<MULTI_LINE_DOCS_COMMENT>"*/"                   { if(docs) ECHO; BEGIN(INITIAL); }


[[:space:]]?"/*".*"*/"[[:space:]]?	        { printf(" "); }

%%

int yywrap() {
    return 1;
}

int main(int argc, char **argv) {
    if (argc > 1 && strcmp(argv[1], "DOCS=1") == 0) {
        docs = 1;
    }
    return yylex();
}
