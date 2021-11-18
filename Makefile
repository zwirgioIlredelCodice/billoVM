build/main: build/main.o build/billoVM.o build/ht.o
	gcc build/main.o build/billoVM.o build/ht.o -o build/main

build/main.o: main.c
	gcc -c -O main.c -o build/main.o

build/billoVM.o: billoVM.c billoVM.h ht.h
	gcc -c -O billoVM.c -o build/billoVM.o

build/ht.o: ht.c ht.h
	gcc -c -O ht.c -o build/ht.o

run:
	@echo running my great billo
	./billolang.py two.billo one.bbillo
	./build/main one.bbillo

debug:
	./billolang.py two.billo one.bbillo debug

exec:
	@./build/main one.bbillo

clean:
	rm build/main build/*.o