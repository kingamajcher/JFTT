%{
#define YYSTYPE int
#include <iostream>
#include <string>
#define P 1234577

using namespace std;

int yylex();
int yyparse();
int yyerror(string s);

int toGP(int a, int G);

int euclidAlgorithm(int a, int G, int *x, int *y);
int inverseGP(int a, int G);
int divideGP(long int a, int b, int G);

int powerGP(long int a, int power);

string error_message = "";
string RPN = "";
%}

%token NUM
%token ERR
%left '+' '-'
%left '*' '/'
%precedence NEG
%nonassoc '^'

%%

input:
    %empty
    | input line
;

line: 
    expr '\n' { 
            cout << RPN << endl;
            cout << "= " << $1 << endl << endl; 
            RPN = "";
        }
    | error '\n' { 
            if (error_message == "") 
                error_message = "zła składnia";
            cout << "Błąd: " << error_message << endl << endl; 
            RPN = ""; 
            error_message = "";
        }
;

expr: 
    NUM                             { RPN += to_string(toGP($1, P)) + " "; $$ = toGP($1, P); }
    | '-' NUM                       { RPN += to_string(toGP(-$2, P)) + " "; $$ = toGP(-$2, P);}
    | '(' expr ')'                  { $$ = $2; }
    | expr '+' expr                 { RPN += "+ "; $$ = toGP($1 + $3, P); }
    | expr '-' expr                 { RPN += "- "; $$ = toGP($1 - $3, P); }
    | expr '*' expr                 { RPN += "* "; $$ = toGP($1 * $3, P); }
    | expr '^' exponent             { RPN += "^ "; $$ = toGP(powerGP($1, $3), P); }
    | expr '/' expr { 
            RPN += "/ "; 
            if($3 == 0) {
                error_message = to_string($3) + " nie posiada odwrotności w GF(" + to_string(P) + ")";
                YYERROR;
            } 
            else 
            {
                $$ = divideGP($1, $3, P); 
            }
        }
;

exponent:
    NUM                             { RPN += to_string($1) + " "; $$ = toGP($1, P-1); }
    | '-' NUM                       { RPN += to_string(toGP(-$2, P-1)) + " "; $$ = toGP(-$2, P-1);}
;

%%

int toGP(int a, int G) {
    return ((a % G) + G) % G;
}

int euclidAlgorithm(int a, int G, int *x, int *y) {
    if (a == 0) {
        *x = 0;
        *y = 1;
        return G;
    }
    int x1, y1;
    int d = euclidAlgorithm(G%a, a, &x1, &y1);
    *x = y1 - (G/a)*x1;
    *y = x1;
    return d;
}

int inverseGP(int a, int G) {
    int x, y;
    euclidAlgorithm(a, G, &x, &y);
    return toGP(x, G);
}

int divideGP(long int a, int b, int G) {
    long int inverse = inverseGP(b, G);
    return (int)((a*inverse) % G);
}

int powerGP(long int a, int power) {
    int result = a;
    if (power == 0) {
        return 1;
    } 
    else if (power == 1) {
        return a;
    }
    for(int i = 2; i <= power; i++) {
        result = (result * a) % P;
    }
    return result;
}

int yyerror(string s) {	
    return 0;
}

int main()
{
    yyparse();
    return 0;
}
