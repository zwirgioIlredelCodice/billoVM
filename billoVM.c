#include <stdio.h>
#include <stdlib.h>
#include "billoVM.h"
#include "ht.h"

/*void debug_billoVM(billoVM *vm)
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
}*/

void init_billoVM(billoVM *vm)
{
    vm->accumulator = 0;
    vm->program_counter = 0;
    vm->call_stack_pointer = 0;

    ht_create(&vm->memory);

    for (size_t i = 0; i < CALL_STACK_SIZE; i++)
    {
        vm->call_stack[i] = 0;
    }
}

void delate_billoVM(billoVM *vm)
{
    ht_destroy(&vm->memory);
}

void run(billoVM *vm, code program[])
{
    int opcode, operand, value;

    while (1)
    {

        opcode = program[vm->program_counter].opcode;
        operand = program[vm->program_counter].operand;

        value = ht_get(&vm->memory, operand);

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

        case NOT:
            vm->accumulator = ~vm->accumulator;
            (vm->program_counter)++;
            break;

        case LOAD_MEMORY:
            vm->accumulator = value;
            (vm->program_counter)++;
            break;

        case LOAD_CONSTANT:
            vm->accumulator = operand;
            (vm->program_counter)++;
            break;

        case STORE_MEMORY:
            ht_set(&vm->memory, operand, vm->accumulator);
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
        //debug_billoVM(vm);
    }
}