#pragma once
#include <stdlib.h>
#include <stdio.h>

enum opcodes
{
    ADDITION,
    SUBTRACTION,
    DIVISION,
    AND,
    OR,
    XOR,
    NOT,
    LOAD_MEMORY,
    LOAD_CONSTANT,
    STORE_MEMORY,
    JUMP,
    JUMP_CONDITIONAL,
    CALL_FUNCTION,
    RETURN_FUNCTION,
    PRINT,
    HALT
};

#define CALL_STACK_SIZE 10
#define MEMORY_SIZE 20

typedef struct billoVM
{
    int accumulator;
    size_t program_counter;
    size_t call_stack_pointer;

    int call_stack[CALL_STACK_SIZE];
    int memory[MEMORY_SIZE];
} billoVM;

typedef struct code
{
    u_int8_t opcode;
    int operand;
} code;

void debug_billoVM(billoVM *vm);

void init_billoVM(billoVM *vm);

void run(billoVM *vm, code program[]);