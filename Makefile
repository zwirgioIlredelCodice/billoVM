main: main.o billoVM.o
	gcc main.o billoVM.o -o main

main.o: main.c
	gcc -c -O main.c -o main.o

billoVM.o: billoVM.c billoVM.h
	gcc -c -O billoVM.c -o billoVM.o

run:
	./main

clean:
	rm main *.o