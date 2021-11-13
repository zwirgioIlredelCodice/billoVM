#include <stdio.h>
#include <stdlib.h>
#include "billoVM.h"

typedef unsigned char BYTE;

code * read_byte_file(char filename[])
{
    FILE *pFile;
    long lSize;
    char *buffer;
    size_t result;

    pFile = fopen(filename, "rb");
    if (pFile == NULL)
    {
        fputs("File error", stderr);
        exit(1);
    }

    // obtain file size:
    fseek(pFile, 0, SEEK_END);
    lSize = ftell(pFile);
    rewind(pFile);

    // allocate memory to contain the whole file:
    buffer = (char *)malloc(sizeof(char) * lSize);
    if (buffer == NULL)
    {
        fputs("Memory error", stderr);
        exit(2);
    }

    // copy the file into the buffer:
    result = fread(buffer, 1, lSize, pFile);
    if (result != lSize)
    {
        fputs("Reading error", stderr);
        exit(3);
    }

    /* the whole file is now loaded in the memory buffer. */

    // terminate
    fclose(pFile);

    static code *program;
    size_t program_size = lSize / 5; // 1 byte for opcode, 4 bytes for operand
    program = (code *)malloc(sizeof(code) * program_size);

    int ii = 0;
    BYTE opcode;
    BYTE b1, b2, b3, b4;
    short operand;

    for (int i = 0; i < program_size; i++) {
        opcode = buffer[ii];
        ii++;
        b1 = buffer[ii];
        ii++;
        b2 = buffer[ii];
        ii++;
        b3 = buffer[ii];
        ii++;
        b4 = buffer[ii];
        ii++;
        operand = (b1<<24) + (b2<<16) + (b3<<8) + b4; //trasfor 4 btyes in int
        program[i].opcode = opcode;
        program[i].operand = operand;
        //printf("opcode=%x , operand=%d\n", program[i].opcode, program[i].operand);
    }

    free(buffer);
    return program;
}

int main( int argc, char *argv[])
{   
    if (argc == 2) {
        code *program;
        program = read_byte_file(argv[1]);

        billoVM vm;
        init_billoVM(&vm);

        run(&vm, program);

        delate_billoVM(&vm);
    }
    else
    {
        printf("file name not in arguments -> EXIT");
    }
}