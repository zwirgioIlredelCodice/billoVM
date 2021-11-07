#pragma once
#include <stdlib.h>
#include <stdio.h>
#include "ht.h"

enum opcodes
{
    LOAD_C,
    ADDITION_C,
    SUBTRACTION_C,
    MULTIPLICATION_C,
    DIVISION_C,
    AND_C,
    OR_C,
    XOR_C,
    NOT_C,
    ADDITION,
    SUBTRACTION,
    DIVISION,
    AND,
    OR,
    XOR,
    NOT,
    LOAD_MEMORY,
    STORE_MEMORY,
    DELATE_MEMORY,
    JUMP,
    JUMP_CONDITIONAL,
    CALL_FUNCTION,
    RETURN_FUNCTION,
    PRINT_ACCUMULATO,
    PRINT_MEMORY,
    HALT
};

#define CALL_STACK_SIZE 10

typedef struct billoVM
{
    int accumulator;
    size_t program_counter;
    size_t call_stack_pointer;

    int call_stack[CALL_STACK_SIZE];
    ht memory;
} billoVM;

typedef struct code
{
    unsigned char opcode;
    int operand;
} code;

//void debug_billoVM(billoVM *vm);

void init_billoVM(billoVM *vm);

void delate_billoVM(billoVM *vm);

void run(billoVM *vm, code program[]);