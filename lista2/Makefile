# Makefile

all: zad1 zad2 zad3 zad4

zad1:
	flex zad1.l
	gcc lex.yy.c -o zad1 -lfl
	./zad1 < cases/test1a.txt > test1results.txt
	cat test1results.txt

zad2:
	flex zad2.l
	gcc lex.yy.c -o zad2 -lfl
	./zad2 < cases/test2.adb > test2results.adb
	cat test2results.adb

zad3:
	flex zad3.l
	gcc lex.yy.c -o zad3 -lfl
	./zad3 < cases/test3.cpp > test3results.cpp
	cat test3results.cpp

zad3_docs:
	flex zad3.l
	gcc lex.yy.c -o zad3 -lfl
	./zad3 DOCS=1 < cases/test3.cpp > test3results.cpp
	cat test3results.cpp
		
zad4:
	flex zad4.l
	gcc lex.yy.c -o zad4 -lfl
	./zad4 cases/test4.txt

run2: zad2
	gnatmake test2results.adb
	./test2results
	
run3: zad3
	g++ -Icases/include -o test3results test3results.cpp
	./test3results
	
run3_docs: zad3_docs
	g++ -Icases/include -o test3results test3results.cpp
	./test3results

clean:
	rm -f lex.yy.c zad1 zad2 zad3 zad4 test1results.txt test2results.adb test2results.ali test2results.o test3results.cpp test2results  test3results

.PHONY: all zad1 zad2 zad3 zad3_docs zad4 run2 run3 clean

