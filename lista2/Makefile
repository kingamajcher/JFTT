# Makefile

all: zad1 zad2 zad3

zad1:
	flex zad1.l
	gcc lex.yy.c -o zad1 -lfl
	./zad1 < cases/test1a.txt > test1results.txt

zad2:
	flex zad2.l
	gcc lex.yy.c -o zad2 -lfl
	./zad2 < cases/test2.adb > test2results.adb

zad3:
	flex zad3.l
	gcc lex.yy.c -o zad3 -lfl
	./zad3 < cases/test3.cpp > test3results.cpp

zad3_docs:
	flex zad3.l
	gcc lex.yy.c -o zad3 -lfl
	./zad3 DOCS=1 < cases/test3.cpp > test3results.cpp
	
print1: zad1
	cat test1results.txt
	
print2: zad2
	cat test2results.adb
	
print3: zad3
	cat test3results.cpp

run2: zad2
	gnatmake test2results.adb
	./test2results
	
run3: zad3
	g++ -Icases/include -o test3results test3results.cpp
	./test3results

clean:
	rm -f lex.yy.c zad1 zad2 zad3 test1results.txt test2results.adb test2results.ali test2results.o test3results.cpp test2results  test3results

.PHONY: all zad1 zad2 zad3 zad3_docs run2 run3 print1 print2 print3 clean

