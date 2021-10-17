#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

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

void debug_billoVM(billoVM *vm)
{

    printf("accumulator= %d\n", vm->accumulator);

    printf("memory= ");
    for (size_t i = 0; i < MEMORY_SIZE; i++)
    {
        printf("%d ", vm->memory[i]);
    }
    printf("\nstack= ");
    for (size_t i = 0; i < CALL_STACK_SIZE; i++)
    {
        printf("%d ", vm->call_stack[i]);
    }
    printf("\n");
}

void init_billoVM(billoVM *vm)
{
    vm->accumulator = 0;
    vm->program_counter = 0;
    vm->call_stack_pointer = 0;

    for (size_t i = 0; i < MEMORY_SIZE; i++)
    {
        vm->memory[i] = 0;
    }

    for (size_t i = 0; i < CALL_STACK_SIZE; i++)
    {
        vm->call_stack[i] = 0;
    }
}

void run(billoVM *vm, code program[], size_t program_size)
{
    int opcode, operand, value;

    while (true)
    {
        if (vm->program_counter > program_size)
        {
            printf("program counter too big -> EXIT\n");
            return;
        }
        opcode = program[vm->program_counter].opcode;
        operand = program[vm->program_counter].operand;

        if (vm->call_stack_pointer > CALL_STACK_SIZE)
        {
            printf("call stack pointer too big -> EXIT\n");
            return;
        }

        if (operand > MEMORY_SIZE)
        {
            value = 0;
        }
        else
        {
            value = vm->memory[operand];
        }

        switch (opcode)
        {

        case ADDITION:
            vm->accumulator += value;
            (vm->program_counter)++;
            break;

        case SUBTRACTION:
            vm->accumulator -= value;
            (vm->program_counter)++;
            break;

        case AND:
            vm->accumulator &= value;
            (vm->program_counter)++;
            break;

        case OR:
            vm->accumulator |= value;
            (vm->program_counter)++;
            break;

        case XOR:
            vm->accumulator ^= value;
            (vm->program_counter)++;
            break;

        case NOT: //safe
            vm->accumulator = ~vm->accumulator;
            (vm->program_counter)++;
            break;

        case LOAD_MEMORY:
            vm->accumulator = value;
            (vm->program_counter)++;
            break;

        case LOAD_CONSTANT: //safe
            vm->accumulator = operand;
            (vm->program_counter)++;
            break;

        case STORE_MEMORY:
            vm->memory[operand] = vm->accumulator;
            (vm->program_counter)++;
            break;

        case JUMP:
            vm->program_counter = operand;
            break;

        case JUMP_CONDITIONAL:
            if (vm->accumulator == 0)
                vm->program_counter = operand;
            else
                (vm->program_counter)++;
            break;

        case CALL_FUNCTION:
            vm->call_stack[vm->call_stack_pointer] = ++(vm->program_counter);
            (vm->call_stack_pointer)++;
            vm->program_counter = operand;
            break;

        case RETURN_FUNCTION:
            vm->program_counter = vm->call_stack[--(vm->call_stack_pointer)];
            break;

        case PRINT:
            printf("%d\n", vm->accumulator);
            (vm->program_counter)++;
            break;

        case HALT:
            return;
        }
        debug_billoVM(vm);
    }
}

int main()
{
    code program[] =
        {
            {LOAD_CONSTANT, 5},
            {STORE_MEMORY, 0},
            {CALL_FUNCTION, 4},
            {HALT, 0},
            {ADDITION, 0},
            {PRINT, 0},
            {RETURN_FUNCTION, 0}};

    billoVM vm;
    init_billoVM(&vm);

    run(&vm, program, 7);
}