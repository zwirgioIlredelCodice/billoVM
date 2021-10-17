main: main.o billoVM.o ht.o
	gcc main.o billoVM.o ht.o -o main

main.o: main.c
	gcc -c -O main.c -o main.o

billoVM.o: billoVM.c billoVM.h
	gcc -c -O billoVM.c -o billoVM.o

ht.o: ht.c ht.h
	gcc -c -O ht.c -o ht.o

run:
	./main

clean:
	rm main *.o